class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
           return len(nums) != len(set(nums))
           #set() method is used to convert any of the iterable to sequence of iterable elements with distinct elements, commonly called Set. 
        
        
        # my wrong approach
#         for i in nums:
#             for j in nums:
#                 if i == j:       --- doesnt work cause will compare same element also.
#                     return True
#         return False
           
#           for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j: continue       --- more time
#                 if nums[i] == nums[j]:
#                     return True
#           return False
            
                