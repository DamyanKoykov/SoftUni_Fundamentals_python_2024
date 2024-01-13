egg_needed = 1  # pack needed per loaf
flour_needed = 1  # kg needed per loaf
milk_needed = 0.250  # ml needed per loaf

budget = float(input())
flour_price_per_kg = float(input())
egg_price_per_pack = flour_price_per_kg * 0.75
milk_price_per_ltr = flour_price_per_kg * 1.25

price_per_loaf = flour_price_per_kg * flour_needed + egg_price_per_pack * egg_needed + milk_price_per_ltr * milk_needed
loafs_made = budget // price_per_loaf
money_left = budget - (price_per_loaf * loafs_made)
coloured_eggs = 0
for i in range(1, int(loafs_made) + 1):
    coloured_eggs += 3
    if i % 3 == 0:
        coloured_eggs -= (i - 2)

print(f"You made {int(loafs_made)} loaves of Easter bread! Now you have {int(coloured_eggs)} eggs and {money_left :.2f}BGN left.")
