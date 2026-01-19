class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        longest = 0
        ourk = 0
        
        for r in range(len(nums)):
            if nums[r] == 0:
                ourk += 1
            
            # If we've used more than k flips, shrink the window from the left
            #Make the window valid again
            while ourk > k:
                if nums[l] == 0:
                    ourk -= 1       #intresting!!
                l += 1
            
            # The window [l, r] is always valid here
            longest = max(longest, r - l + 1)

        return longest