#这是一个井字棋盘游戏
theBoard={'top-L':' ','top-W':' ','top-R':' ','mid-L':' ','mid-W':' ','mid-R':' ','low-L':' ','low-W':' ','low-R':' '}
def printBoard(board):
    print(board['top-L'] +'|'+board['top-W']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] +'|'+board['mid-W']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['low-L'] +'|'+board['low-W']+'|'+board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for '+turn +'. Move on which space?')
    move=input()
    theBoard[move] = turn
    if turn=='X':
        turn=='0'
    else:
        turn='X'
printBoard(theBoard)