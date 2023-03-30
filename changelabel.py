import os
import random
import numpy as np
from numpy import *
import cv2

# this is needed when you delete some class in the middle


txtfilepath = "F:\TUM22WS\mydata\labels"  # orignal txt file
savefilepath = "F:\TUM22WS\mydata\labela"  # changed txt file


total_txt = os.listdir(txtfilepath)
num = len(total_txt)
list = range(num)
files = os.listdir(savefilepath)


for i in list:  # go through txt files
    name = total_txt[i]
    readfile = open(txtfilepath + "/" + name, 'r')
    fline = readfile.readlines()
    savetxt = open(savefilepath + "/" + name, 'w+')

    for temp in fline:

        list2 = temp.split()  # split the text by ' ' according to YOLOv7 label format

        if list2[0] == '1':
            list2[0] = '1'  # 1 to 1
        elif list2[0] == '2':
            list2[0] = '2'  # 2 to 2
        elif list2[0] == '3':
            list2[0] = '3'  # 3 to 3
        elif list2[0] == '4':
            list2[0] = '4'  # 4 to 4
        elif list2[0] == '5':
            list2[0] = '5'  # 5 to 5
        elif list2[0] == '6':
            list2[0] = '6'  # 6 to 6
        elif list2[0] == '8':
            list2[0] = '6'  # 8 to 6 here we merge rat and mouse
        elif list2[0] == '9':
            list2[0] = '7'  # 9 to 7
        elif list2[0] == '0':
            list2[0] = '0'  # 0 to o
        b = " ".join(list2)
        savetxt.write(b)  # rewrite
        savetxt.write('\n')

