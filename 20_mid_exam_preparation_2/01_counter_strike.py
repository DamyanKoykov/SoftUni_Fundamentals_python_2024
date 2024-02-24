def counter_strike_main():
    energy = int(input())
    wins_count = 0

    while True:
        command = input()

        if command == "End of battle":
            return print(f"Won battles: {wins_count}. Energy left: {energy}")

        else:

            if isinstance(battle_(energy, command, wins_count), tuple):
                energy, wins_count = battle_(energy, command, wins_count)
            else:
                print(battle_(energy, command, wins_count))
                break


def battle_(energy_, command_, wins):
    command = int(command_)

    if energy_ >= command:
        energy_ -= command
        wins += 1
        if wins % 3 == 0:
            energy_ += wins
        return energy_, wins

    else:
        return (f"Not enough energy! Game ends with "
                f"{wins} won battles and {energy_} energy")


counter_strike_main()
