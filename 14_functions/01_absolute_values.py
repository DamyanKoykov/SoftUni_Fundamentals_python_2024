# nums_as_string = input().split()
#
# num_list = [abs(float(char)) for char in nums_as_string]
# print(num_list)

nums_as_string = input()


def absolute_values(string):
    output = [abs(float(char)) for char in string.split()]
    return print(output)


absolute_values(nums_as_string)
