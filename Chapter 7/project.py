#!/usr/bin/python3 
#This is the sixth chapter of the project combat
#获取密码
import re 
pw = input('请输入密码： ')
#检查是否符合要求
def checkpw(pw):
    chpwd = re.compile(r'[0-9]+').search(pw)
    ch_len = re.compile(r'.{8,}').search(pw)
    ch_lowerCase = re.compile(r'[a-z]').search(pw)
    ch_uperCase = re.compile(r'[A-Z]').search(pw)
    if ch_len != None:
        if ch_lowerCase and chpwd and ch_uperCase !=None:
            print('输入的密码符合要求')
        else:
            print('输入的密码必须包含大小写和数字')
    else:
        print('密码必须不少于8位，请重新输入密码')
checkpw(pw)