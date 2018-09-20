power_number = eval(input('Enter a power: '))
number_of_digit = eval(input('How many digit do you want? '))
print('The last ', number_of_digit, ' digit(s) of 2^', power_number, ' is ', (2**power_number)%(10**number_of_digit), sep='')

