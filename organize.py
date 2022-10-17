import os
import shutil

source_dir = "C:\\Users\\prana\\Downloads"
destination_dir = "C:\\Users\\prana\\Downloads\\DownloadedImages"

list_of_files = os.listdir(source_dir)
ext_list = []

for file in list_of_files:
    name, ext = os.path.splitext(file)
    if(ext == ''):
        continue
    if ext in ['.png', '.jpeg', '.jpg', '.gif', '.gfif']:
        path1 = source_dir + "/" + file    
        path2 = destination_dir
        path3 = destination_dir + "/" + file
        print(path1, path2, path3)
        if(os.path.exists(path2)):
            print('Moving')
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
#     else:
#         ext_list.append(ext)
#     unique_ext = set(ext_list)
# print(unique_ext)