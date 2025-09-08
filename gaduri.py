from math import sqrt,pi,acos,radians,floor,degrees

x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())

c_length = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) #중심간거리

if r1 == r2:
    len = 2 * pi * r1 + 2 * c_length
    extent = pi * (r1 ** 2) + c_length * (2 * r1)
else:
    r_b, r_s = (r1, r2) if r1 > r2 else (r2, r1)

    tan_length = sqrt(c_length * c_length - (r_b - r_s) ** 2) #접선길이

    angle = degrees(acos(((r_b - r_s) ** 2 + c_length ** 2 - tan_length ** 2) / (2 * c_length * (r_b - r_s))))

    real_angle = 360 - (2 * angle)

    one_length = r_b * radians(real_angle)
    two_length = r_s * radians(2 * angle)
    circle1_extent = 0.5 * r_b * r_b * radians(real_angle)
    circle2_extent = 0.5 * r_s * r_s * radians(2 * angle)

    len = 2 * tan_length + one_length + two_length #총길이

    trapezoid = (r1 + r2) * tan_length #사다리꼴넓이

    extent = trapezoid + circle1_extent + circle2_extent #총넓이

print(floor(extent), floor(len))
