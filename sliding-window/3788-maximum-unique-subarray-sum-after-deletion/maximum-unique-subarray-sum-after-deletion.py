class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniqueset = set()
        maxnumber = max(nums)
        maxsum = 0
        for i in range(len(nums)):
            if nums[i] >=0 and nums[i] not in uniqueset:
                maxsum += nums[i]
                uniqueset.add(nums[i])

        return maxsum if maxsum > 0 else maxnumber
    

#Main obstacle - How to handle negative numbers
#set is not indexable → uniqueset[i] will crash

#Oneliner - return sum({v for v in nums if v>0}) or max(a)