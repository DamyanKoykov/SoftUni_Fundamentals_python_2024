data_type = input()
string_input = input()


def data_type_convertor(command, data):
    if "int" in command:
        return print(int(data) * 2)
    elif "real" in command:
        return print(f"{(float(data) * 1.5):.2f}")
    elif "string" in command:
        return print(f"${data}$")


data_type_convertor(data_type, string_input)
