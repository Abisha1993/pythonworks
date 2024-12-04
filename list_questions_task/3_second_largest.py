def find_second_largest(nums):
    if len(nums)<2:
        return "list should have at least two elements."
    unique_nums=list(set(nums))
    if len(unique_nums)<2:
        return "there is no second largest element."
    unique_nums.sort(reverse=True)
    return unique_nums[1]
numbers=[10,20,4,45,99,99,20]
second_largest=find_second_largest(numbers)
print(f"the second element is:{second_largest}")