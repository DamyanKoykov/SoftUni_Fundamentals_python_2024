divisor = int(input())
limiter = int(input())

for num in range(limiter, divisor - 1, -1):
    if num % divisor == 0 and num > 0:
        print(num)
        break
