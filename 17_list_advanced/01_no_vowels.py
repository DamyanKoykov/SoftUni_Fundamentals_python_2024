def remove_vowels(word: str):
    vowels_list = ["a", "o", "u", "e", "i", "A", "O", "U", "E", "I"]
    return "".join([char for char in word if char not in vowels_list])


print(remove_vowels(input()))
