def schedule_modifier(schedule: list):
    while True:
        command = input().split(":")
        if "course start" in command:
            break
        if ("Add" in command) and (command[1] not in schedule):
            schedule.append(command[1])
        elif ("Insert" in command) and (command[1] not in schedule):
            schedule.insert(int(command[2]), command[1])
        elif ("Remove" in command) and (command[1] in schedule):
            schedule.remove(command[1])
        elif ("Swap" in command) \
                and (any(command[1] in lesson for lesson in schedule)) \
                and (any(command[2] in lesson for lesson in schedule)):
            lesion_1 = None
            lesson_2 = None
            for index, current_lesson in enumerate(schedule):
                if command[1] in current_lesson:
                    lesion_1 = index
                elif command[2] in current_lesson:
                    lesson_2 = index
            schedule[lesion_1], schedule[lesson_2] \
                = schedule[lesson_2], schedule[lesion_1]
        elif "Exercise" in command:
            if command[1] in schedule:
                exercise_index = (schedule.index(command[1])) + 1
                schedule.insert(exercise_index, f"{command[1]}-Exercise")
            else:
                schedule.append(command[1])
                schedule.append(f"{command[1]}-Exercise")
    for index, current_lesion in enumerate(schedule):
        print(f"{index + 1}.{current_lesion}")


initial_schedule = input().split(", ")
schedule_modifier(initial_schedule)
