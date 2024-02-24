def lift(people_count, lifts_wagons):
    lifts_wagons = list(map(int, lifts_wagons.split()))
    wagon_capacity = 4
    output1 = ""
    for index, current_seats_taken in enumerate(lifts_wagons):
        if current_seats_taken < wagon_capacity:
            if (current_seats_taken + people_count) > wagon_capacity:
                lifts_wagons[index] = wagon_capacity
            else:
                lifts_wagons[index] = current_seats_taken + people_count
            people_count -= (wagon_capacity - current_seats_taken)
        if people_count < 0:
            output1 = "The lift has empty spots!\n"
            break
    if people_count > 0:
        output1 = (f"There isn't enough space! "
                   f"{people_count} people in a queue!\n")
    return print(output1 + " ".join(str(char) for char in lifts_wagons))


queue_count = int(input())
wagons = input()
lift(queue_count, wagons)
