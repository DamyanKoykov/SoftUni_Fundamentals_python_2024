from functools import reduce

nums = [1, 2, 3, 4, 5]

print(reduce(lambda x, y: x + y**2, filter(lambda x: x % 2 == 0, nums)))