current_version = input()
new_version = int("".join(current_version.split("."))) + 1
new_version = [str(num) for num in str(new_version)]
output = ".".join(new_version)
print(output)
