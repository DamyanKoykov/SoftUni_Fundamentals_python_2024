words = input().split()


def even_len_words(tex: list):
    even_words = [word for word in words if len(word) % 2 == 0]
    return print("\n".join(even_words))


even_len_words(words)
