string_of_digits = input()
count_of_beggars = int(input())

# gets string_of_digits and converts it to list of integers
list_of_integers = list(map(int, string_of_digits.split(",")))
beggars_profit = []
for current_beggar in range(count_of_beggars):  # create a list with 0 profit for all beggars
    beggars_profit.append(0)
while list_of_integers:  # while the list is not empty
    for current_beggar in range(count_of_beggars):  # calculate the profit and save it to beggar_profit list
        if list_of_integers:  # if the list is not empty
            beggars_profit[current_beggar] += list_of_integers[0]
            list_of_integers.pop(0)
        else:  # the list is empty
            break
print(beggars_profit)
