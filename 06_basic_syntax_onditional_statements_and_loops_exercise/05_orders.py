order_count = int(input())

total_price = 0

for current_order in range(order_count):
    capsule_price = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 > capsule_price or capsule_price > 100 or\
            1 > days or days > 31 or\
            1 > capsules_needed_per_day or capsules_needed_per_day > 2000:
        print()
        continue
    else:
        order_price = capsule_price * capsules_needed_per_day * days
        print(f"The price for the coffee is: ${order_price :.2f}")
        total_price += order_price

print(f"Total: ${total_price :.2f}")
