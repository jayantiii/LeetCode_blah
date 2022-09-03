class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res
        
        
        
        
        
        
        
#         # my soln
#         for i in range(len(nums)):
            
#             n = nums.pop(0)
#             if n in nums:
#                 j = nums.index(n)
#                 nums.pop(j)
#             else: return n
                
            
            
        
        