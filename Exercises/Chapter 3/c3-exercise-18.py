p = int(100*(eval(input('Enter the amount ($): '))))
q = p//25
p = p%25
d = p//10
p = p%10
n = p//5
p = p%5
print(q,'quarter(s) -', d, 'dime(s) -', n, 'nickel(s) -', p, 'penny(pennies)')