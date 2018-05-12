import glob
import csv
import re
import shutil
import os

dataset_old_folder = 'pwTextOnly'
dataset_new_folder = 'New_Data_year'

if not os.path.exists(dataset_new_folder):
    os.mkdir(dataset_new_folder)

# This function finds the file and saves it in a different folder then rename it
def copy_rename(old_file_name, new_file_name):
    # old_file_name is the PMID
    # new_file_name is the year_PMID
    src_dir = os.curdir + '/' + dataset_old_folder + '/'
    dst_dir = os.path.join(os.curdir, dataset_new_folder)
    src_file = os.path.join(src_dir, old_file_name + '.txt')
    shutil.copy2(src_file, dst_dir)

    dst_file = os.path.join(dst_dir, old_file_name + '.txt')
    new_dst_file_name = os.path.join(dst_dir, new_file_name + '.txt')
    os.rename(dst_file, new_dst_file_name)


# This part picks each file from pwTextOnly and rename the file and places it in the folder-New_Data
# Also there are suppose to be 13871 files but we have only 11052 files in pwTextOnly folder
# NB: not all the files in pwTextOnly folder can be found in pyruvateKinase_warburg.csv


files = glob.glob(dataset_old_folder + '/*.txt')
print(len(files))
csv_file = open('csv/pyruvateKinase_warburg.csv', 'r', encoding='utf8')
csv_file_reader = csv.reader(csv_file, delimiter=',')

for fname in files:
    file_exist_in_csv = False
    fname1 = re.findall(r'\d+', fname.rsplit(sep='\\')[-1])
    # fname1 is the PMID retrieved by stripping all alphabets leaving the numbers. fname1 is return as a list
    csv_file.seek(0)  # resets the reader iterator position to the first row
    for row in csv_file_reader:
        # checks the PMID in csv against the filename if they are the same
        if row[0] == fname1[0]:
            year = row[2]
            new_name = year + '_' + fname1[0]
            file_exist_in_csv = True
            break
    if file_exist_in_csv:
        copy_rename(fname1[0], new_name)
    else:
        print(fname1[0]+' does not have a year')
        copy_rename(fname1[0],'0000_'+fname1[0])

print('file rename has ended')
