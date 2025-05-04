class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # hint - Track the smallest (first) and second smallest (second) seen so far.
        first = float('inf')
        second = float('inf')

        for x in nums:
            if x <=first: # dont forget x <=
                first = x
            elif x <=  second: # dont forget equal sign
                second = x
            else:
                return True # means x is the third
        return False
     

#  i started like this, confusing with no startegy
#  i = 0
#         j=1
#         k=2
#         while True:
#             if nums[i] > nums[j]:
#                 k = k +1
#                 while True:

#another
    #   first, second = inf, inf
        
    #     for third in nums:
            
    #         if second < third: return True
    #         if third <= first: first= third    
    #         else:  second = third 
                
    #     return  False



        