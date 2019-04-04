#!/usr/bin/python3
# findFile ----find file
import os
import re
path=input('Please enter the path: ')
search_key=input('Please enter search keywords: ')
#create a function
def search_file(search_key,path): 
    #Determine if the path is correct
    if  os.path.exists(path):
        #Traverse all directories under path
        for root,dirs,files in os.walk(path):
            #Find the files that meet the requirements and print
            for file in files:
                fileNameList = re.compile(search_key).search(file)
                if  fileNameList ==None:
                    continue
                else:
                    print(os.path.join(root, file))
    #Empty return exit
    elif path == '':
        print('exit')
    #Error return 
    else:
        print('You enter the wrong path！')
search_file(search_key,path)
print('Done')