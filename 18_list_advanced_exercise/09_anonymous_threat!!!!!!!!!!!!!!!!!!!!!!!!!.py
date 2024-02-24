def merge(start, stop, message):
    if int(start) < (len(message) - 1):
        if int(stop) > (len(message) - 1):
            stop = len(message) - 1
        for index in range(int(start), int(stop)):
            message[int(start)] += message.pop(int(start) + 1)
            return message


def divide(index_to_divide, divider, message):
    if int(index_to_divide) < (len(message) - 1):
        step = len(message) // divider
        for char in message[index_to_divide]:
            message[index_to_divide] = []


def decode_message():
    secret_message = input().split()
    command = ""
    while True:
        if command == "3:1":
            break
        command, index_1, index_2 = input().split()
        if command == "merge":
            secret_message = merge(index_1, index_2, secret_message)
        elif command == "divide":
            secret_message = divide(index_1, index_2, secret_message)

