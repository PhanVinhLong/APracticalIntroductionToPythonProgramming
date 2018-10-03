t = eval(input('Enter a temperature: '))
unit = eval(input('Which unit is it? (1 = Celsius, 2 = Fahrenheit) '))
if unit==1:
    new_t = 9/5*t+32
    print(new_t, 'fahrenheit')
elif unit==2:
    new_t = 5/9*(t-32)
    print(new_t, 'celcius')
else:
    print('Error')