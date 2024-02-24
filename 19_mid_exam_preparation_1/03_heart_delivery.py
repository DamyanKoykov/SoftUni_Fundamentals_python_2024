def cupid_game(neighbourhood: str):
    neighbourhood = list(map(int, neighbourhood.split("@")))
    command = input().split()
    current_position = 0
    while "Love!" not in command:
        jump_length = int(command[1])
        # check if jump is in range
        if (current_position + jump_length) < len(neighbourhood):
            current_position += jump_length
        else:  # if not in range we go back in the beginning
            current_position = 0
        if neighbourhood[current_position] == 0:
            print(f"Place {current_position} already had Valentine's day.")
        else:
            neighbourhood[current_position] -= 2
            if neighbourhood[current_position] == 0:
                print(f"Place {current_position} has Valentine's day.")
        command = input().split()
    failed_households = 0
    for index, house in enumerate(neighbourhood):
        if house > 0:
            failed_households += 1
    output = f"Cupid's last position was {current_position}.\n"
    if failed_households:
        output += f"Cupid has failed {failed_households} places."
    else:
        output += "Mission was successful."
    return print(output)


neighbourhood_input = input()
cupid_game(neighbourhood_input)
