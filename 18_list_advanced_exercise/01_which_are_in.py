sequence_to_look_for = input().split(", ")
list_to_check = input().split(", ")

output = []
for current_sequence in sequence_to_look_for:
    for current_word in list_to_check:
        if current_sequence in current_word:
            output += [current_sequence]
            break
print(output)
