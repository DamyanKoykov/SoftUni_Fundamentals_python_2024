numbers = list(map(int, input().split(", ")))

indices = [index for index, current_num in enumerate(numbers)
           if current_num % 2 == 0]

print(indices)
