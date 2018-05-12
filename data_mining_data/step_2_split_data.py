import glob
import numpy as np
import os
import pandas as pd

# Change this to the name of the folder where your dataset is
dataset_name = 'New_Data'

files = glob.glob('./train/*.npy')

if not os.path.exists('valid'):
    os.mkdir('valid')
if not os.path.exists('test'):
    os.mkdir('test')

df = pd.read_csv('./unigram.txt', delimiter='\t',header=None)
cnt = df[2].values
cnt = 1.0*cnt/cnt.sum()
print(len(files))
error_file = open('Error_Step_2.txt','w+')# holds files name that caused error
for fname in files:
    dat = np.load(fname)
    prob = np.random.uniform(0,1,dat.shape)
    p = 1 - np.sqrt((10.0**(-5))/cnt[dat])
    dat = dat[prob > p]

    split = int(0.1 * len(dat))
    try:
        i = np.random.randint(len(dat))
    except ValueError:
        print('fname: '+fname+' i: '+str(i))
        error_file.write('fname: '+fname+' i: '+str(i)+'\n')
        pass

    dat = np.roll(dat, i)
    test_dat = dat[:split]
    dat = dat[split:]

    dat = np.roll(dat, i)
    valid_dat = dat[:split]
    dat = dat[split:]

    np.save(fname.replace('train','test'), test_dat)
    np.save(fname.replace('train','valid'), valid_dat)
    np.save(fname, dat)
error_file.close()
print('step_2_split_data has ended\n\n')