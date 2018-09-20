year = eval(input('Enter a year: '))
sub = abs(1600-year)
a = sub//4
b = sub//100
c = sub//400
d = a - b + c
e = 0
for i in range(1601, year+1):
    if((i%4==0 and i%100!=0) or i%400==0):
        e = e+1
print(d, e)
