nums = input()
#  converts the string to list
nums = nums.split(", ")
# converts the string in the list to int
nums = list(map(int, nums))
counter = 0
for index in range(len(nums)):
    if nums[index] != 0:
        nums[index], nums[counter] = nums[counter], nums[index]
        counter += 1
print(nums)
