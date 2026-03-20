from functools import reduce
nums = [1, 2, 3, 4]
print(list(map(lambda x: x*2, nums)))      # [2,4,6,8]
print(list(filter(lambda x: x>2, nums)))   # [3,4]
print(reduce(lambda x, y: x+y, nums))      # 10