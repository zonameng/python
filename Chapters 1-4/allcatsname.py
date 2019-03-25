#!/usr/bin/python3
catNames=[]
while True:
    name=input('Please enter the name'+str(len(catNames)+1) +'of the cat,'+'Or enter nothing to stop: ')
    print(name)
    if name == '':
        break
catNames=catNames+[name]
print('The names of these cats are:')
for name in catNames:
    print('  '+ name)