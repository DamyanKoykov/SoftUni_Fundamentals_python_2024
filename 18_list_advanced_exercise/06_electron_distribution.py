def electron_distribution(electrons_count):
    current_shell = 1
    shells = []
    while electrons_count > 0:
        shell_capacity = 2 * current_shell ** 2
        atoms_in_current_shell = min(electrons_count, shell_capacity)
        shells.append(atoms_in_current_shell)
        electrons_count -= atoms_in_current_shell
        current_shell += 1
    return print(shells)


available_electrons = int(input())
electron_distribution(available_electrons)
