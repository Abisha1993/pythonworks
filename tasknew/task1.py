def find_closet_to_zero(nums):
    nums.sort(key=lambda x:(abs(x), -x))
    return nums[0]
nums1=[-4,-2,1,4,8]


print(find_closet_to_zero(nums1))

