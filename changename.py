import os
import re
import sys


#this script is to change the class in the label files. The wrong setting in data augmentation generates images with the same file name in each folder,
# and there are conflicts when moving to the same folder.



path = 'D://Downloads//auge//'
#'marten','mouse','hedgehog',
nam=['cat','fox','marten','mouse','hedgehog','bird']
num=[101,102,103,104,105,106]

#change name
for na in nam:
    fileList = os.listdir(path+na+"//image")  # Path to files need to be changed
    print("before：" + str(fileList))  # print the file list
    ind=nam.index(na)
    nu=num[ind]

    currentpath = os.getcwd()  #current work path
    os.chdir(path)  # change path to target path
    n = 1  #flag
    for fileName in fileList:
        pat = ".+\.(jpg|png|jpeg)"  # find images with regex
        pattern = re.findall(pat, fileName)
        os.rename(os.path.join(path+na+"//image", fileName), (str(nu) + "_aug"+fileName.replace("png","") + pattern[0]))  # rename
        n += 1

    os.chdir(currentpath)  # change back to original path
    sys.stdin.flush()

#change label
for na in nam:
    fileList = os.listdir(path + na + "//label")  # Path to files need to be changed
    print("修改前：" + str(fileList))  # print the file list
    ind=nam.index(na)
    nu=num[ind]

    currentpath = os.getcwd()  #current work path
    os.chdir(path)  # change path to target path
    n = 1  #flag
    for fileName in fileList:
        pat = ".+\.(txt)"  # find images with regex
        pattern = re.findall(pat, fileName)
        os.rename(os.path.join(path+na+"//label", fileName), (str(nu) + "_aug"+fileName.replace("txt","") + pattern[0])) # rename
        n += 1

    os.chdir(currentpath)
    sys.stdin.flush()
#
# for na in nam:
#     fileList = os.listdir(path)
#     print("before：" + str(fileList))
#     ind=nam.index(na)
#     nu=num[ind]
#
#     currentpath = os.getcwd()
#     os.chdir(path)
#     n = 1
#     for fileName in fileList:
#         pat = ".+\.(txt)"
#         pattern = re.findall(pat, fileName)
#         os.rename(os.path.join(path, fileName), (str(nu) + "_aug"+fileName.replace("txt","") ))
#         n += 1
#
#     os.chdir(currentpath)
#     sys.stdin.flush()

