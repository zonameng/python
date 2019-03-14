for i in range(1, 10):
    for j in range(1, i+1):
        #print(j,i)
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()