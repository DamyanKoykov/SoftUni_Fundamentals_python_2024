employees_happiness = input().split()
factor_of_improvement = int(input())


def office_happiness(employees_happiness_list: list, improvement_factor: int):
    employees_happiness_list = list(
        map(lambda num: int(num) * improvement_factor,
            employees_happiness_list))

    over_average_happy_employees_list = list(filter(
        lambda num: num >= sum(employees_happiness_list) / len(
            employees_happiness_list), employees_happiness_list))

    happy_employee_count = len(over_average_happy_employees_list)
    total_employee_count = len(employees_happiness_list)
    if happy_employee_count >= (total_employee_count / 2):
        return print(f"Score: {happy_employee_count}/{total_employee_count}."
                     f" Employees are happy!")
    else:
        return print(f"Score: {happy_employee_count}/{total_employee_count}."
                     f" Employees are not happy!")


office_happiness(employees_happiness, factor_of_improvement)
