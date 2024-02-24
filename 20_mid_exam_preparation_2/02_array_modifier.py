def array_mod_main(array: list):
    while True:
        command = input().split()
        if "end" in command:
            return print(", ".join(map(str, array)))
        elif "swap" in command:
            array = swap(array, int(command[1]), int(command[2]))
        elif "multiply" in command:
            array = multiply(array, int(command[1]), int(command[2]))
        elif "decrease" in command:
            array = decrease(array)


def swap(array_, i_1, i_2):
    array_[i_1], array_[i_2] = array_[i_2], array_[i_1]
    return list(array_)


def multiply(array_, i_1, i_2):
    array_[i_1] *= array_[i_2]
    return list(array_)


def decrease(array_):
    array_ = [num - 1 for num in array_]
    return list(array_)


array_input = list(map(int, input().split()))
array_mod_main(array_input)
