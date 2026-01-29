#1: break at 5
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

#2: break after 3
x = 1
while True:
    if x > 3:
        break
    print(x)
    x += 1

#3: break at 7
y = 0
while y < 10:
    if y == 7:
        break
    print(y)
    y += 2

#4: break countdown
n = 10
while n > 0:
    if n == 5:
        break
    print(n)
    n -= 1

#5: break multiple of 3
k = 1
while k < 20:
    if k % 3 == 0:
        break
    print(k)
    k += 1
