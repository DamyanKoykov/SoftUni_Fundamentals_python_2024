people_lst = input()
step = int(input())

people_lst = people_lst.split()
people_lst = list(map(int, people_lst))
dead_list = []
index = 0
while len(people_lst) > 0:
    index = (index + step - 1) % len(people_lst)
    dead_list.append(people_lst[index])
    people_lst.pop(index)

print("[", end="")
for num in people_lst:
    print()
