def train_function(command: str, wagons):
    command = command.split()
    if "add" in command:
        return adding_people(wagons, int(command[1]))
    elif "insert" in command:
        return inserting_people(wagons, int(command[1]), int(command[2]))
    elif "leave" in command:
        return people_leaving(wagons, int(command[1]), int(command[2]))


def adding_people(wagons, count):
    wagons[- 1] += count
    return wagons


def inserting_people(wagons, index, count):
    wagons[index] += count
    return wagons


def people_leaving(wagons, index, count):
    wagons[index] -= count
    return wagons


wagon_count = int(input())
wagon_list = [0 for counter in range(wagon_count)]
user_input = ""
while True:
    if user_input == "End":
        print(wagon_list)
        break
    else:
        user_input = input()
        train_function(user_input, wagon_list)


