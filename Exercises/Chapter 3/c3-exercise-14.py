from math import pi, sin
angle_in_degree = eval(input('Enter an angle in degree: '))
angle_in_radius = angle_in_degree*pi/180
print('sin(', angle_in_degree, ') = ', round(sin(angle_in_radius), 4), sep='')