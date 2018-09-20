p = 100*(eval(input('Enter the amount ($): ')))
q = p//25
p = p-q*25
d = p//10
p = p-10*d
n = p//5
p = p-n*5
print(q,' quarter(s) - ', d, ' dime(s) - ', n, ' nickel(s) - ', p, ' penny(pennies)')
