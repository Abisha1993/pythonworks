def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
        right = 1
    for i in range(n -1, -1, -1):
        answer [i] *= right
        right *= nums [i]
        return answer
nums = [1,2,3,4]
print(product_except_self(nums))