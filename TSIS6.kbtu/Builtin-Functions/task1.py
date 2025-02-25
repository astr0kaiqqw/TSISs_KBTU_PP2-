import math

def multiply_list(numbers):
    return math.prod(numbers)

nums = [2, 3, 4, 5]
result = multiply_list(nums)
print("Произведение всех чисел в списке", result)