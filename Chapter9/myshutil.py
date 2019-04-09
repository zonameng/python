#!/usr/bin/python3.6
import os
import shutil
myfiles='f:\\tes.txt'
chfiles='f:\\tesgd.txt'
os.open(myfiles,os.O_CREAT)
shutil.copyfile(myfiles,chfiles)
#shutil.move(chfiles,'f:\\pytext')
shutil.rmtree('f:\\pytext')
for folderName, subfolders,fileanmes in os.walk('e:\\'):
    pass
print('Done')