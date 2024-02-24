def sort_numbers(numbers: str):
    num_list = list(map(int, numbers.split(", ")))
    positive_list = [str(num) for num in num_list if num >= 0]
    negative_list = [str(num) for num in num_list if num < 0]
    even_list = [str(num) for num in num_list if num % 2 == 0]
    odd_list = [str(num) for num in num_list if num % 2 != 0]

    print("Positive:", ", ".join(positive_list))
    print("Negative:", ", ".join(negative_list))
    print("Even:", ", ".join(even_list))
    print("Odd:", ", ".join(odd_list))


numbers_input = input()
sort_numbers(numbers_input)
