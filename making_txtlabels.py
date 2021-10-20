import json
import os
import random
import math

# set your datasets
data = "bowl9" # change datset name
train_ratio = 0.8 # test ratio = 1 - train_ratio

name_list = os.listdir('new_dataset/'+ data + '/labels/3D_json')
for i in name_list:
    with open('new_dataset/'+ data + '/labels/3D_json/'+ i,'r') as f:
        data2 = json.load(f)
        
        location = data2['labelingInfo'][0]['3DBox']['location'][0]
        k = open('new_dataset/'+ data + '/labels/using_data/' + i[-21:-5] + '.txt','w')
        k.write('3 ')
        k.write(str(float(location['x9'])/1280))
        k.write(' ')
        k.write(str(float(location['y9'])/720))
        k.write(' ')
        k.write(str(float(location['x4'])/1280))
        k.write(' ')
        k.write(str(float(location['y4'])/720))
        k.write(' ')
        k.write(str(float(location['x1'])/1280))
        k.write(' ')
        k.write(str(float(location['y1'])/720))
        k.write(' ')
        k.write(str(float(location['x8'])/1280))
        k.write(' ')
        k.write(str(float(location['y8'])/720))
        k.write(' ')
        k.write(str(float(location['x5'])/1280))
        k.write(' ')
        k.write(str(float(location['y5'])/720))
        k.write(' ')
        k.write(str(float(location['x3'])/1280))
        k.write(' ')
        k.write(str(float(location['y3'])/720))
        k.write(' ')
        k.write(str(float(location['x2'])/1280))
        k.write(' ')
        k.write(str(float(location['y2'])/720))
        k.write(' ')
        k.write(str(float(location['x7'])/1280))
        k.write(' ')
        k.write(str(float(location['y7'])/720))
        k.write(' ')
        k.write(str(float(location['x6'])/1280))
        k.write(' ')
        k.write(str(float(location['y6'])/720))
        k.write(' ')
        k.write(str(float(location['x-range'])/1280))
        k.write(' ')
        k.write(str(float(location['y-range'])/720))
        k.write(' ')

data_root = os.path.join('new_dataset', data, 'labels/using_data')
loader_root = os.path.join('data', data)

name_list2 = os.listdir(data_root)
image_list = [name for name in name_list2 if name[-4:] == '.txt']
train_len = math.floor(len(image_list) * train_ratio)

train_name = random.sample(image_list, train_len)
valid_name = [name for name in image_list if name not in train_name]

with open(os.path.join(loader_root, 'train.txt'), 'w') as file:
    for i in range(len(train_name)):
        file.write(os.path.join(data_root.replace('labels','origin').replace('using_data','Images'), train_name[i].replace('.txt','.png') + '\n'))
    
with open(os.path.join(loader_root, 'test.txt'), 'w') as file:
    for i in range(len(valid_name)):
        file.write(os.path.join(data_root.replace('labels','origin').replace('using_data','Images'), valid_name[i].replace('.txt','.png') + '\n'))
