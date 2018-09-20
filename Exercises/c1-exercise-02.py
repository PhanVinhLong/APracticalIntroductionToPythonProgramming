num_of_rows = 4
num_of_columns = 20
print('*'*num_of_columns)
for i in range(num_of_rows - 2):
    print('*', ' '*(num_of_columns - 2), '*', sep='')
print('*'*num_of_columns)
