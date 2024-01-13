coffee_needed = 0
list_of_events = ["coding", "dog", "cat", "movie"]

while True:
    event = input()
    if event == "END":
        break
    elif event.lower() in list_of_events:
        if event.isupper():
            coffee_needed += 2
        else:
            coffee_needed += 1

if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)
