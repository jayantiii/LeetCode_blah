class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n),0(1)
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

#optimal way (O(n)) - have one prefix and one suffix product arrays ( should try)
#   res = [1] * (len(nums))
#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res

# same answer as submitted, just see how written from neetcode
    #    prod, zero_cnt = 1, 0
    #     for num in nums:
    #         if num:             -- if nums =0 , then false!
    #             prod *= num
    #         else:
    #             zero_cnt +=  1
    #     if zero_cnt > 1: return [0] * len(nums)

    #     res = [0] * len(nums)
    #     for i, c in enumerate(nums):
    #         if zero_cnt: res[i] = 0 if c else prod
    #         else: res[i] = prod // c
    #     return res


        
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

#brute force is to use 2 nested for loops