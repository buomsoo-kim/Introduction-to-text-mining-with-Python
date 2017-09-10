for i in range(1, 10):
    for j in range(1, 10):
        if j != 9:
            print('{} * {} ='.format(i, j), i*j, end = '  ')
        else:
            print('{} * {} ='.format(i, j), i*j)