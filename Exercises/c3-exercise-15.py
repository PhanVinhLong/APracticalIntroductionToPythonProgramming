from math import pi, sin, cos
for i in range(0, 346, 15):
    angle_in_radius = i*pi/180
    sin_result = sin(angle_in_radius)
    cos_result = cos(angle_in_radius)
    print(i, '---', round(sin_result, 4), round(cos_result, 4))

