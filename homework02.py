import random

numbers = list(random.randint(1,10) for _ in range(6))
print(numbers)
def get_create(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups


print(get_create(numbers))