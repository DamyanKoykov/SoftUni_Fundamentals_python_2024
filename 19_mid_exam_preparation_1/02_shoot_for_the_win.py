def shooting_range_game():
    targets_list = list(map(int, input().split()))
    command = input()
    shot_targets_counter = 0
    while command != "End":
        shot_index = int(command)
        if ((0 <= shot_index < len(targets_list))
                and (targets_list[shot_index] != -1)):
            # if the shot is within range:
            shot_targets_counter += 1
            current_target_value = targets_list[shot_index]
            targets_list[shot_index] = -1
            for index, current_target in enumerate(targets_list):
                if current_target != -1:
                    if current_target > current_target_value:
                        targets_list[index] -= current_target_value
                    else:
                        targets_list[index] += current_target_value
        command = input()
    return print(f"Shot targets: {shot_targets_counter} -> "
                 f"{' '.join(list(map(str, targets_list)))}")


shooting_range_game()
