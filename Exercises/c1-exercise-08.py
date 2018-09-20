num1, num2, num3 = input('Enter three numbers: ').split()
num1 = eval(num1)
num2 = eval(num2)
num3 = eval(num3)
total = num1+num2+num3
average = total/3
print('Total = ', total, '; ', 'Average = ', average, sep='')
