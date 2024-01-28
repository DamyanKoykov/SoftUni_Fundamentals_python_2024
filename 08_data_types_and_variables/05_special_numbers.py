limiter = int(input())

num_sum = 0
is_it_special = False

for current_num in range(1, limiter + 1):
    for num_checker in range(1, len(str(current_num)) + 1):
        num_sum += int(str(current_num)[num_checker - 1])
    if num_sum == 5 or num_sum == 7 or num_sum == 11:
        is_it_special = True
    num_sum = 0
    print(f"{current_num} -> {is_it_special}")
    is_it_special = False
