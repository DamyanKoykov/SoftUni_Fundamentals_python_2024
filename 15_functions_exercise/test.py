number_input = int(input())
divider_input = int(input())


def factorial_division(num, divider):
    result = num
    for factor in range(num - 1, 0, -1):
        result *= factor
    result /= divider
    return print(f"{result:.2f}")


factorial_division(number_input, divider_input)