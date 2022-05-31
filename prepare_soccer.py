import os
from shutil import copyfile
from glob import glob
import numpy as np
from tqdm import tqdm
from PIL import Image
import cv2
import shutil
# You only need to change this line to your dataset download path
download_path = '../data/tracking'


save_path = download_path + '/pytorch'
if not os.path.isdir(save_path):
    os.mkdir(save_path)
    

train_path = download_path + '/bounding_box_train'
train_save_path = download_path + '/pytorch/train'
# val_save_path = download_path + '/pytorch/val'
# if not os.path.isdir(train_save_path):
#     os.mkdir(train_save_path)
#     os.mkdir(val_save_path)

# train_videos = glob(download_path+"/train/*")
# test_videos = glob(download_path+"/test/*")

# for video_num, video in enumerate(list(train_videos) + list(test_videos)):
#     det = np.load(os.path.join(video, 'gt/gt.npy'), allow_pickle=True).item()
#     imgs = glob(os.path.join(video, 'img1/*.jpg'))
#     imgs = sorted(imgs, key=lambda x: int(x.split('/')[-1].split('.')[0]))
#     for img in tqdm(imgs):
#         box_feats = {}
#         num = img.split('/')[-1].split('.')[0]
#         num = int(num)
#         img = Image.open(img)
#         img = np.array(img)
#         # print(det[num])
#         for track, box in det[num].items():
#             ID = str(video_num).zfill(3) + str(track).zfill(3)
#             box = [box[0], box[1], box[0]+box[2], box[1]+box[3]]
#             if box[0] == box[2]: continue
#             if not os.path.exists(os.path.join(val_save_path, ID)):
#                 os.mkdir(os.path.join(val_save_path, ID))
#                 # os.mkdir(os.path.join(train_save_path, ID))
#                 cv2.imwrite(os.path.join(val_save_path, ID, f'{track+box[0]}.jpg'), img[box[1]:box[3], box[0]:box[2], ::-1])
#             else:
#                 if not os.path.exists(os.path.join(train_save_path, ID)):
#                     os.mkdir(os.path.join(train_save_path, ID))
#                 cv2.imwrite(os.path.join(train_save_path, ID, f'{track+box[0]}.jpg'), img[box[1]:box[3], box[0]:box[2], ::-1])


# for val in glob(os.path.join(val_save_path, '*')):
#     if not os.path.exists(val.replace('val', 'train')):
#         shutil.rmtree(val)

save_path = download_path + '/small'
if not os.path.isdir(save_path):
    os.mkdir(save_path)

total_folders = glob(os.path.join(train_save_path, '*'))
length = len(total_folders)
small = int(length*0.05)

selected_folders = np.random.choice(total_folders, small, replace=False)

for video in selected_folders:
    shutil.copytree(video, os.path.join(save_path, 'train', video.split('/')[-1]))
    shutil.copytree(video.replace('train', 'val'), os.path.join(save_path, 'val', video.split('/')[-1]))