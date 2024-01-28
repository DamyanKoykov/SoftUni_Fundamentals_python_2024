gifts_as_string = input()
command = ""
gifts_as_list = gifts_as_string.split()  # converts gifts string in to list so we can iterate
while command != "No Money":
    command = input()
    command_as_list = command.split()  # converts the command in list so we can iterate
    if "OutOfStock" in command:  # we have to replace the item from the list with "None"
        for index in range(len(gifts_as_list)):
            if gifts_as_list[index] == command_as_list[1]:  # iterate trough gift list to look fo item to replace
                gifts_as_list[index] = "None"
        command_as_list = []  # reset the command list for next iteration
    elif "Required" in command:  # we have to replace the gift list index with the gift from the command
        command_index_as_int = int(command_as_list[2])  # gets the index from command as int
        if command_index_as_int in range(len(gifts_as_list)):
            gifts_as_list[command_index_as_int] = command_as_list[1]
        command_as_list = []  # reset the command list for next iteration
    elif "JustInCase" in command:  # we have to replace the last item in gift list with gift from command
        gifts_as_list[-1] = command_as_list[1]
        command_as_list = []  # reset the command list for next iteration

for item in gifts_as_list:
    if item != "None":
        print(item, end=" ")
