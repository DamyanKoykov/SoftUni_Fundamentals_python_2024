def inventory_func(inventory_: list):
    command = input()
    while command != "Craft!":

        command = command.split(" - ")
        if "Collect" in command and command[1] not in inventory_:
            inventory.append(command[1])

        elif "Drop" in command and command[1] in inventory_:
            inventory_.remove(command[1])

        elif "Combine Items" in command:

            items_to_combine = command[1].split(":")
            if items_to_combine[0] in inventory_:
                index = inventory_.index(items_to_combine[0])
                inventory_.insert(index + 1, items_to_combine[1])

        elif "Renew" in command and command[1] in inventory_:
            inventory_.remove(command[1])
            inventory_.append(command[1])

        command = input()

    return ", ".join(inventory_)


inventory = input().split(", ")
print(inventory_func(inventory))
