def memory_game(sequence: list):
    command = input().split()
    moves = 0
    while "end" not in command:
        moves += 1
        index_1 = int(command[0])
        index_2 = int(command[1])
        if (index_1 == index_2
                or index_1 < 0
                or index_2 < 0
                or (index_2 > (len(sequence) - 1))):
            middle = len(sequence) // 2
            sequence.insert(middle, f"-{moves}a")
            sequence.insert(middle, f"-{moves}a")
            print("Invalid input! Adding additional elements to the board")
        elif sequence[index_1] == sequence[index_2]:
            element = sequence.pop(index_1)
            sequence.remove(element)
            print(f"Congrats! You have found matching elements - {element}!")
        else:
            print("Try again!")
        if not sequence:
            return print(f"You have won in {moves} turns!")
        command = input().split()
    print(f"Sorry you lose :(\n{' '.join(sequence)}")


sequence_input = input().split()
memory_game(sequence_input)
