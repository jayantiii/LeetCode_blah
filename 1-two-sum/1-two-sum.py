class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}   # idea in notes
        for i in range(len(nums)):
            sec = target - nums[i]
            if sec in dic:
                return[i,dic[sec]]
            else:
                dic[nums[i]] = i
                
#  My approach - takes more time :/            
       
#         for i,n in enumerate(nums):
#             for j,m in enumerate(nums):
#                 if i==j:continue
#                 if n+m == target:
#                     return [i,j]
  
        