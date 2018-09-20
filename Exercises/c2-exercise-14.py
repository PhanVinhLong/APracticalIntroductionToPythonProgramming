num = eval(input('Enter the high of the diamond: '))
temp = int((num+1)/2)
for i in range(1, temp, 1):
    print(' '*(temp-i), '*'*i, sep='')
