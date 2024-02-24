def cath_them_all(pokemons_list):
    output = 0
    while pokemons_list:
        index = int(input())
        if index < 0:
            captured_pokemon = pokemons_list[0]
            pokemons_list[0] = pokemons_list[-1]
        elif index > (len(pokemons_list) - 1):
            captured_pokemon = pokemons_list[-1]
            pokemons_list[-1] = pokemons_list[0]
        else:
            captured_pokemon = pokemons_list.pop(index)
        for current_index in range(len(pokemons_list)):
            if pokemons_list[current_index] <= captured_pokemon:
                pokemons_list[current_index] += captured_pokemon
            elif pokemons_list[current_index] > captured_pokemon:
                pokemons_list[current_index] -= captured_pokemon
        output += captured_pokemon
    return print(output)


pokemons = list(map(int, (input().split())))
cath_them_all(pokemons)
