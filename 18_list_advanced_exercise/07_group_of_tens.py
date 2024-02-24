def groups_of_tens(nums):
    nums = nums.split(", ")
    current_group_limit = 10
    while len(nums) > 0:
        current_group = []
        current_group = [int(num) for num in nums
                         if int(num) <= current_group_limit]
        print(f"Group of {current_group_limit}'s: {current_group}")
        for num in current_group:
            nums.remove(str(num))
        current_group_limit += 10


nums_string = input()
groups_of_tens(nums_string)
