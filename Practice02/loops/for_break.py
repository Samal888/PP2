#1: break at 5
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#2: break after 3
for j in range(1, 10):
    if j > 3:
        break
    print(j)

#3: break at 6
for k in range(0, 10, 2):
    if k == 6:
        break
    print(k)

#4: break countdown
for n in range(10, 0, -1):
    if n == 5:
        break
    print(n)

#5: break first multiple of 3
for x in range(1, 20):
    if x % 3 == 0:
        break
    print(x)
