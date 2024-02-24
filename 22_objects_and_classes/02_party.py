class Party:
    def __init__(self):
        self.people = []


party = Party()

while True:
    command = input()

    if command == "End":
        break
    else:
        guest = command
        party.people.append(guest)

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
