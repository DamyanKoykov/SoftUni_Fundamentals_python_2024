class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if "mammal" == species:
            zoo.mammals.append(name)

        elif "fish" == species:
            zoo.fishes.append(name)

        elif "bird" == species:
            zoo.birds.append(name)

        zoo.__animals += 1

    def get_info(self, species):
        if species == "mammal":
            return (f"Mammals in {zoo_name_}: {', '.join(self.mammals)}\n"
                    f"Total animals: {zoo.__animals}")
        elif species == "fish":
            return (f"Fishes in {zoo_name_}: {', '.join(self.fishes)}\n"
                    f"Total animals: {zoo.__animals}")
        elif species == "bird":
            return (f"Birds in {zoo_name_}: {',     '.join(self.birds)}\n"
                    f"Total animals: {zoo.__animals}")


zoo_name_ = input()
animals_count = int(input())

zoo = Zoo(zoo_name_)
for index in range(animals_count):
    species_, animal_ = input().split()
    zoo.add_animals(species_, animal_)

get_species_info = input()
print(zoo.get_info(get_species_info))
