string_of_nums = input()
delete_count = int(input())

num_list = list(map(int, string_of_nums.split()))  # converts string_of_nums in list of integers
for delete_counter in range(delete_count):
    num_list.remove(min(num_list))  # deletes the smallest num in the list
result = ", ".join(map(str, num_list))  # map converts int to str and .join concatenates the list
print(result)
