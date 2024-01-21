word = input().lower()

total_count = 0
search_for = ["sand", "water", "fish", "sun"]

for current_word in search_for:
    counter = word.count(current_word)
    if counter > 0:
        total_count += counter
print(total_count)
