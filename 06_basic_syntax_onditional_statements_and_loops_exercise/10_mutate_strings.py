string1 = input()
string2 = input()

list1 = []
list2 = []
for char in string1:
    list1.append(char)
for char in string2:
    list2.append(char)

for i in range(len(list1)):
    if list1[i] != list2[i]:
        list1[i] = list2[i]
        print("".join(list1))
    else:
        continue
