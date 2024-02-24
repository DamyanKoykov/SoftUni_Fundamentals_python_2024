def decipher_message(message):
    deciphered_words = []

    for word in message.split():
        # Swap the second and last letters
        swapped_word = word[0] + word[-1] + word[2:-1] + word[1]

        # Replace the first letter with its character code
        decoded_word = chr(int(swapped_word[0])) + swapped_word[1:]

        deciphered_words.append(decoded_word)

    return ' '.join(deciphered_words)


# Example usage:
secret_message = "72olle 103doo 100ya"
deciphered_message = decipher_message(secret_message)
print("Deciphered message:", deciphered_message)
