#!/usr/bin/python3
def listtest(spam):
    spam.insert(-1,'and')
    a=','.join(spa)
    print(a)
spa=['apples','bananas','tofu','cats']
listtest(spa)


grid=[['.','.','.','.','.','.'],
      ['.','0','0','.','.','.'],
      ['0','0','0','0','.','.'],
      ['0','0','0','0','0','.'],
      ['.','0','0','0','0','0'],
      ['0','0','0','0','0','.'],
      ['0','0','0','0','.','.'],
      ['.','0','0','.','.','.'],
      ['.','.','.','.','.','.']]

for i in range(len(grid[0])):
      for b in range(len(grid)):
            #print(i,b)
            print(grid[b][i],end=' ')
      print('\n')

      