import os
import shutil

for each_file in os.listdir("/scratch/gilbreth/li2068/UNETR/BTCV/dataset/Dataset300_synrad/imagesTr"):
    new_name = "_".join(each_file.split('_')[0:2])+".nii.gz"
    new_name = os.path.join("/scratch/gilbreth/li2068/UNETR/BTCV/dataset/Dataset300_synrad/imagesTs",new_name)
    old_file = os.path.join("/scratch/gilbreth/li2068/UNETR/BTCV/dataset/Dataset300_synrad/imagesTs", each_file)
