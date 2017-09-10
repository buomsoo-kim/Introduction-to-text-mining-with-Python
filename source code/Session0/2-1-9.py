l = [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'J'], ['K', 'L', 'M', 'N', 'O']]
for row in l:
    for column in row:
        print(column.lower(), end = ' ')
    print('\n')