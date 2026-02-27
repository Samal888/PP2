import math
# 1
degree = float(input("Input degree: "))
radian = degree * math.pi / 180
print("Output radian:", round(radian, 6))
# 2
height = float(input("\nHeight: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
trapezoid_area = 0.5 * (base1 + base2) * height
print("Area of trapezoid:", trapezoid_area)
# 3
n = int(input("\nInput number of sides: "))
s = float(input("Input the length of a side: "))
polygon_area = (n * s * s) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(polygon_area))
# 4
base = float(input("\nLength of base: "))
h = float(input("Height of parallelogram: "))
parallelogram_area = base * h
print("Area of parallelogram:", parallelogram_area)