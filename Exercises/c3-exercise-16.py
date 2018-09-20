import math
Y = eval(input('Enter year: '))
C = Y//100
m = (15+C-(math.floor(C/4))-(math.floor((8*C+13)/25)))%30
n = (4+C-(math.floor(C/4)))%7
a = Y%5
b = Y%7
c = Y%19
d = (19*c + m)%30
e = (2*a+4*b+6*d+n)%7
day = (22+d+e)%32+1
month = 3+(22+d+e)//32
if(d==29 and e==6):
    month = 4
    day = 19
if((d==28 and e==6) and (m=2 or m=5 or m=10 or m=13 or m=16 or m=21 or m=24 or m=39)):
    month = 4
    day = 18
print(month, day, Y, sep='-')

