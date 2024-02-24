rooms_count = int(input())

free_chairs_total = 0
this_room_needs_chair = []
enough_chairs = True
for current_room_index in range(1, rooms_count + 1):
    room_info = input().split()
    if len(room_info[0]) >= int(room_info[1]):
        free_chairs_total += (len(room_info[0]) - int(room_info[1]))
    else:
        enough_chairs = False
        chairs_needed_for_current_room = (
                int(room_info[1]) - len(room_info[0]))
        this_room_needs_chair.append(
            [chairs_needed_for_current_room, current_room_index])

if enough_chairs:
    print(f"Game On, {free_chairs_total} free chairs left")
else:
    for room in this_room_needs_chair:
        print(f"{room[0]} more chairs needed in room {room[1]}")