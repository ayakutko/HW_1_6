import math
# 14
def is_even(value):
    return value%2 == 0

value = 5
if is_even(value):
    print("Even")
else:
    print("Not even")
#15
def is_intersecting(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    sum_radius = r1 + r2
    return sum_radius <= distance

x1 = 2
y1 = 3
r1 = 4
x2 = 5
y2 = 6
r2 = 7
if is_intersecting(x1, x2, r1, x2, y2, r2):
    print("Intersecting")
else:
    print("Not intersecting")
#16
def is_confronting(v1, v2):
    total_s = 10
    s1 = 4
    s2 = total_s - s1
    t = s1/v1
    s_before_turn = t*v2
    return s_before_turn >= s2
v1 = 2
v2 = 1
if is_confronting(v1, v2):
    print("Confront")
else:
    print("Will not confront")
#17
def quadric_equation(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        x1 = ((-b + math.sqrt(d))/(2*a))
        x2 = ((-b - math.sqrt(d))/(2*a))
        return x1, x2
    else:
        return "No Roots"

print(quadric_equation(1, 23, 2))





