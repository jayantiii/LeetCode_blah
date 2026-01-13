class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i,x in enumerate(nums):
            if nums[i] != i:
                return nums[i] -1 

# ## this below is important if nums = [0,1] and last number 2 is missing
            if nums[i] == len(nums) -1:
                return x + 1 



# one line!
#return sum(range(len(nums)+1)) - sum(nums)