def find_closet_to_zero(nums):
    nums.sort(key=lambda x:(abs(x), -x))
    return nums[0]

nums2=[2,-1,1]

print(find_closet_to_zero(nums2))

