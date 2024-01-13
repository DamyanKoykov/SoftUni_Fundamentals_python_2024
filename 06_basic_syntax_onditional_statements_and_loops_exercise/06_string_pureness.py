string_count = int(input())

for _ in range(1, string_count + 1):
    word = input()
    for char in word:
        if char == "," or char == "." or char == "_":
            print(f"{word} is not pure!")
            break
    else:
        print(f"{word} is pure.")
