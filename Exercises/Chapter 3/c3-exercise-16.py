from math import floor
Y = eval(input('Enter year: '))
C = (Y+1)//100
m = (15+C-(floor(C/4))-(floor((8*C+13)/25)))%30
n = (4+C-(floor(C/4)))%7
a = Y%4
b = Y%7
c = Y%19
d = (19*c+m)%30
e = (2*a+4*b+6*d+n)%7
if((22+d+e)>31):
    day = d+e-9
    month = 4
else:
    day = 22+d+e
    month = 3
if(d==29 and e==6):
    month = 4
    day = 19
if((d==28 and e==6) and (m==2 or m==5 or m==10 or m==13 or m==16 or m==21 or m==24 or m==39)):
    month = 4
    day = 18
print(month, day, Y, sep='-')