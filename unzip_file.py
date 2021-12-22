import os
import shutil
import zipfile
from os.path import join, getsize


# 解压文件
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:     
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)       
    else:
        print('This is not zip')
        

unzip_file("../mnt/flower_data.zip","./")