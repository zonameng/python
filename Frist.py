#!/usr/bin/python3
#This program says hellp and asks for my name 
print('Hello World!')
print('What is your name?')
MyName=input()
print('It is good to meet you,'  +  MyName)
print('The length of your name is: '+ str(len(MyName)))
#print(len(MyName))
print('What is your age?')
MyAge=input()
print('You will be ' + str(int(MyAge)+1)+' in a year.')