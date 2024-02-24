def decipher_message(secret_message: list):
    result = ""
    for index, word in enumerate(secret_message):
        first_letter_ord = "".join(filter(lambda char: char.isdigit(), word))
        swapped_word = (f"{chr(int(first_letter_ord))}"
                        + word[(len(first_letter_ord))::])
        swapped_word = [char for char in swapped_word]
        swapped_word[1], swapped_word[-1] = swapped_word[-1], swapped_word[1]
        result += ("".join(swapped_word) + " ")
    return print(result)


message_input = input().split()
decipher_message(message_input)
