time = eval(input('Enter hour: '))
time_ahead = eval(input('How many hours ahead? '))
print('New hour: ', (time+time_ahead-1)%12+1, ' o\'clock', sep='')
