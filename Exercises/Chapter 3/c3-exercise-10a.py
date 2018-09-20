power_number = eval(input('Enter a power: '))
print('The last 2 digits of 2^', power_number, ' are ', (2**power_number)%100, sep='')