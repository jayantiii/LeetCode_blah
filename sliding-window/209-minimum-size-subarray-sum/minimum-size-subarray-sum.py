class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
# Sliding window
        l,r = 0,0
        minlen = float("inf")
        currsum = 0
        for r in range(len(nums)):
            currsum += nums[r]
            while currsum >= target:
                minlen = min(minlen, r-l+1) 
                currsum = currsum - nums[l] #dont forget to do this
                l+=1
        return 0 if minlen == float("inf") else minlen

            


#Use a sliding window approach:

# Expand the window by moving the right pointer, adding elements to the current sum.
# When the sum ≥ target, try to shrink from the left to find the minimal length.
# Track the minimum window length that satisfies the condition.
# This runs in O(n) time since each element is processed at most twice.

#Note, just cause using while loop in for loop doesnt mean time is more

#Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).