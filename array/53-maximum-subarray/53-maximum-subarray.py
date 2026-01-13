class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        l = len(nums)
        for i in range(1,l):
            if nums[i-1] > 0:
                nums[i] = nums[i] +nums[i-1]
        return max(nums)
            
            
            
        
#     cool answer, even use one-line with the accumulate  ?? didnt understand

# from itertools import accumulate
#     return max(accumulate(nums, lambda x, y: x+y if x > 0 else y))
                
                
           
# You can cut the if-condition out and use the max() function too if you want to REALLY be concise ;)

#     for i in range(1,len(nums)):
#         nums[i] = max(nums[i], nums[i-1] + nums[i])
#     return max(nums)