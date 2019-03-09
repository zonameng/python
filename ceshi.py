#!/usr/bin/python3
#This is a Collatz 序列 ! 
def Collatz(Num):
    if Num%2==0:
        print(Num//2)
    elif Num%2==1:
        print(3*Num+1)
while True:
    try:
        a=int(input('请输入数字: '))
        number=Collatz(a)
    except ValueError:
        print('你输入的是非整数，请重新输入')
    
    