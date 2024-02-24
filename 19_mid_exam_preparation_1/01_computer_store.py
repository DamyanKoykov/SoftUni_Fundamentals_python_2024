def computer_store():
    discount = 1
    total_cost_no_vat = 0
    total_cost_with_vat = 0
    vat_price = 0
    while True:
        command = input()
        if ("special" not in command) and ("regular" not in command):
            command = float(command)
            if command < 0:
                print("Invalid price!")
            else:
                total_cost_no_vat += command
                vat_price = total_cost_no_vat * 0.20
                total_cost_with_vat = total_cost_no_vat * 1.20
        else:
            if "special" in command:
                discount = 0.90
            if total_cost_no_vat <= 0:
                print("Invalid order!")
                break
            else:
                return print(
                    f"Congratulations you've just bought a new computer!\n"
                    f"Price without taxes: {total_cost_no_vat:.2f}$\n"
                    f"Taxes: {vat_price:.2f}$\n"
                    f"-----------\n"
                    f"Total price: {total_cost_with_vat * discount:.2f}$"
                    )


computer_store()
