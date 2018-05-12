import glob
import pathlib
import os

dataset_old_folder = 'New_Data_year'
dataset_new_folder = 'New_Data_stopwords'

# word_tokenize accepts a string as an input, not a file.
stop_words = open('stop_words.txt', 'r').read().split()  # read stops into a list
files = glob.glob(dataset_old_folder + '/*.txt')

if not os.path.exists(dataset_new_folder):
    os.mkdir(dataset_new_folder)
for fname in files:
    file = open(fname)
    # Use this to read file content as a stream then into a list:
    words = file.read().split()
    appendFile = open(fname.replace(dataset_old_folder+'\\', dataset_new_folder+'/'), 'w+')

    for r in words:
        if not r.lower() in stop_words:
            appendFile.write(" "+r)
    appendFile.close()
print('end')

