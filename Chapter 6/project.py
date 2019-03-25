#!/usr/bin/python3 
#This is the sixth chapter of the project combat
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
def findMaxLen(listData):
    maxLen = 0
    for i in range(len(listData)):
        if maxLen < len(listData[i]):
            maxLen = len(listData[i])
    return maxLen
def printTable():
    subListLen = len(tableData)     # 列表tableData中子列表的个数
    colWidths = [0]*subListLen      # 保存每一个列表的最大宽度,*操作符可以用于一个列表和一个整数，实现列表的复制
    ListNum = len(tableData[0])     # 每个子列表的元素个数（假设相等）
    for i in range(subListLen):
        colWidths[i] = findMaxLen(tableData[i])
    for i in range(ListNum):
        for j in range(subListLen):
        # print(tableData[j][i].rjust(colWidths[j]+2),end= '')
            print(tableData[j][i].rjust(colWidths[j] ), end=' ')
        print()
printTable()