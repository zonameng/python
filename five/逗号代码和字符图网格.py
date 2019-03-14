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
print(grid[0][0],grid[1][0],grid[2][0],grid[3][0],grid[4][0],grid[6][0],grid[5][0],grid[7][0],grid[8][0])
print(grid[0][1],grid[1][1],grid[2][1],grid[3][1],grid[4][1],grid[6][1],grid[5][1],grid[7][1],grid[8][1])
print(len(grid))
print(len(grid[1]))
for i in range(len(grid[0])):
      for b in range(len(grid)):
            #print(i,b)
            print(grid[b][i],end=' ')
      print('\n')

      