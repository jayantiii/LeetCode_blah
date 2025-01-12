class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = [0]*len(nums) 
        zeroc = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else: zeroc +=1
        if zeroc > 1:
            return res
        for i in range(len(nums)):
            if nums[i] == 0:
                res = [0] * len(nums)
                res[i] = prod
                return res
            else:
                res[i] = prod//nums[i]
        return res



        
#my first idea - this fails when there is zero in array and also ZeroDivisionError
#   res = []
#         ans = 1
#         for i in range(len(nums)):
#             ans *= nums[i]
#         for i in range(len(nums)):
#             res.append(ans//nums[i])
#         return res

#changed to fix(18/24 pass) -> problem when array has more than one zero
 # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         ans *= nums[i]
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         res = [0]*len(nums)
        #         res[i] = ans
        #         return res
        #     else:
        #         res.append(ans//nums[i])
        # return res