#11
import math
def degrees2radians(degrees):
    return degrees*math.pi/180
print(degrees2radians(60), degrees2radians(45), degrees2radians(40))
#12
def sum_of_digits(a):
    b = int(a/100)
    c = int((a-b*100)/10)
    d = int(a-b*100-c*10)
    return b + c + d
print(sum_of_digits(567))
#13
def square_and_perimeter(a, b):
    square_result = 1/2*a*b
    hypothenuze = math.sqrt(a ** 2 + b ** 2)
    perimeter_result = a + b + hypothenuze
    return square_result, perimeter_result,
result1, result2 = square_and_perimeter(3, 4)
print(result1, result2)
