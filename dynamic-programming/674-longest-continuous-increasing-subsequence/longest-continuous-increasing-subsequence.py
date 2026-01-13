class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        maxlen = 1
        currlen= 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currlen = currlen+1
                maxlen = max(maxlen, currlen)
            else:
                currlen = 1 # start again
        return maxlen
