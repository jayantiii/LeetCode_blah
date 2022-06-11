class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter  # better approach
        # print(Counter(nums1) & Counter(nums2))
        # print(Counter(nums1))
        # print(Counter(nums2))
        return (Counter(nums1) & Counter(nums2)).elements()
    
    
# MY code using dict --
#         count = {}
#         res = []
#         for i,num in enumerate(nums1):
#             if num in count:
#                 count[num] +=1
#             else:
#                  count[num] = 1
#         for num in nums2:
#             if num in count and count[num]!=0:
#                 res.append(num)
#                 count[num] -=1
#         return res
                
            
              
        
        
        
        


        