import math
# 1
degree = float(input())
radian = degree * math.pi / 180
print(round(radian, 6))
# 2
height = float(input())
base1 = float(input())
base2 = float(input())
area = 0.5 * (base1 + base2) * height
print(area)
# 3
n = int(input())
s = float(input())
areapol = (n * s * s) / (4 * math.tan(math.pi / n))
print(round(areapol))
# 4
base = float(input())
h = float(input())
parea = base * h
print(parea)