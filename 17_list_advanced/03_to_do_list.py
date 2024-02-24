def to_do_list_main(command, to_do_list):
    if command == "End":
        output = [element for element in to_do_list if element != ""]
        return print(output)
    command = command.split("-")
    to_do_list.pop((int(command[0]) - 1))
    to_do_list.insert((int(command[0]) - 1), command[1])


to_do_notes = ["" for counter in range(10)]
user_input = ""
while user_input != "End":
    user_input = input()
    to_do_list_main(user_input, to_do_notes)
