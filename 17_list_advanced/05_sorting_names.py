names_list = input().split(", ")

names_list = sorted(names_list, key=lambda x: (-len(x), x))
print(names_list)