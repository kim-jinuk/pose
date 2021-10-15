import os
import math
import random

data = 'sause_container4'
train_ratio = 0.8

data_root = os.path.join('new_dataset', data, 'labels/using_data')
#data_root = os.path.join('new_dataset', data, 'labels/direction')
loader_root = os.path.join('data', data)

name_list = os.listdir(data_root)
image_list = [name for name in name_list if name[-4:] == '.txt']
train_len = math.floor(len(image_list) * train_ratio)

train_name = random.sample(image_list, train_len)
valid_name = [name for name in image_list if name not in train_name]

with open(os.path.join(loader_root, 'train.txt'), 'w') as file:
    for i in range(len(train_name)):
        file.write(os.path.join(data_root.replace('labels','origin').replace('using_data','Images'), train_name[i].replace('.txt','.png') + '\n'))
    
with open(os.path.join(loader_root, 'test.txt'), 'w') as file:
    for i in range(len(valid_name)):
        file.write(os.path.join(data_root.replace('labels','origin').replace('using_data','Images'), valid_name[i].replace('.txt','.png') + '\n'))
