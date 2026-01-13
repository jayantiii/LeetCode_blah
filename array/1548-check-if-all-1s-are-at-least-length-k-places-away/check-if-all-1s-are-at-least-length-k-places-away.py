class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev1 = -1
        for i in range(len(nums)):
            if prev1 == -1 and nums[i] ==1:
                prev1 = i
                continue
            
            if nums[i] == 1 and (i - prev1 -1) < k:
                return False

            if nums[i]==1: # this if case should be at last
                prev1 = i

        return True

        