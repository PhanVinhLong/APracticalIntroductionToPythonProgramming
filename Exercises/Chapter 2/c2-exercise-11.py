rows = eval(input('How many row do you want? '))
columns = eval(input('How many column do you want? '))
print('*'*columns)
for i in range(rows-2):
    print('*', ' '*(columns-2), '*', sep='')
print('*'*columns)
