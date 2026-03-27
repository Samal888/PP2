# 1
def squares(n):
    for i in range(n + 1):
        yield i * i
# 2
def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
# 3
def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
# 4
def squares_ran(a, b):
    for i in range(a, b + 1):
        yield i * i
# 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
a = int(input())
b = int(input())

print("\nSquares up to n:")
for x in squares(n):
    print(x)

print("\nEven numbers:")
print(",".join(str(x) for x in even(n)))

print("\nDivisible by 3 and 4:")
for x in divisible(n):
    print(x)

print("\nSquares from a to b:")
for x in squares_ran(a, b):
    print(x)

print("\nCountdown:")
for x in countdown(n):
    print(x)