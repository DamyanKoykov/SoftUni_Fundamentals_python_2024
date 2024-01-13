while True:
    word = input()
    if word == "End":
        break
    elif word == "SoftUni":
        continue
    else:
        for char in word:
            print(char * 2, end="")
    print()