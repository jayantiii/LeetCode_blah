class Solution:
    def rob(self, nums: List[int]) -> int:
#That means the first house is the neighbor of the last one.
#Logic is to run maxrob on all elements without last and also all without first
#Then whichever is max is answer
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        if len(nums) == 2:
            return max(nums[0],nums[1])

        def robmax(numsarr):
            m = len(numsarr)
            maxamount = [0]*m # cause first or last we remove
            maxamount[0] = numsarr[0]
            maxamount[1] = max(numsarr[0],numsarr[1])
            for i in range(2,m):
                    maxamount[i] = max(maxamount[i-1], maxamount[i-2] + numsarr[i] )
            return maxamount[-1] #last
        
        return max(robmax(nums[:-1]),robmax(nums[1:]))













# # the odd/even logic wont work out!!! passed 50/75 cases
#         n = len(nums)
#         maxamount = [0]*len(nums)
#         maxamount[0] = nums[0]

#         if n <=1:
#             return maxamount[n-1]

#         maxamount[1] = nums[1] if nums[1] > nums[0] else nums[0]

#         for i in range(2, len(nums)):
#             robprev = maxamount[i-1]

#             if i-2 == 0 and i == n-1:
#                 robnow = nums[i] 
#             elif i== n-1:
#                 if len(nums) % 2 == 0: # even
#                 print()
#                     robnow = nums[i] + maxamount[i-2]
#                     print(robnow)
#                 else: #odd
#                     maxfirstlast = nums[n-1] if nums[n-1] > maxamount[0] else maxamount[0] 
#                     robnow = maxamount[i-2]
#                 # maxamount[i] = max(robprev, maxamount[i-2] + nums[i])
#             else:
#                 robnow = nums[i] + maxamount[i-2]

#             maxamount[i] = max(robprev,robnow)
#             print(maxamount)

#         return maxamount[n-1]
        