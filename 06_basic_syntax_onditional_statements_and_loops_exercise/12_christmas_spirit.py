decorations_per_day = int(input())
days_left_to_christmas = int(input())

total_cost = 0
christmas_spirit_points = 0
ornament_set_price, ornament_set_points = 2, 5
tree_skirts_price, tree_skirts_points = 5, 3
tree_garlands_price, tree_garland_points = 3, 10
tree_lights_price, tree_lights_points = 15, 17

for current_day in range(1, days_left_to_christmas + 1):
    if current_day % 11 == 0:
        decorations_per_day += 2
    if current_day % 2 == 0:
        total_cost += ornament_set_price * decorations_per_day
        christmas_spirit_points += ornament_set_points
    if current_day % 3 == 0:
        total_cost += (tree_skirts_price + tree_garlands_price) * decorations_per_day
        christmas_spirit_points += (tree_skirts_points + tree_garland_points)
    if current_day % 5 == 0:
        total_cost += tree_lights_price * decorations_per_day
        christmas_spirit_points += tree_lights_points
    if current_day % 3 == 0 and current_day % 5 == 0:
        christmas_spirit_points += 30
    if current_day % 10 == 0:
        christmas_spirit_points -= 20
        total_cost += tree_skirts_price + tree_garlands_price + tree_lights_price
if days_left_to_christmas % 10 == 0:
    christmas_spirit_points -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit_points}")
