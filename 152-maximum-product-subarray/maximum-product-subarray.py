class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmax = nums[0]
        currmin = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                currmax, currmin = currmin, currmax  # <- flip detection/handling
            
            currmax = max(nums[i], currmax*nums[i])
            currmin = min(nums[i],currmin*nums[i])

            best = max(best,currmax)

        return best

        






#I first thought subarray shouldnt have negative to be maximum
#But, remember that 2 negatives make positive

# Trick: negatives flip sign, so you must track both max and min product ending at each index.

# cur_max(i) = maximum product of any subarray that ends exactly at index i
# cur_min(i) = minimum product of any subarray that ends exactly at index i

# cur_min is the “worst (most negative) product of a subarray ending here”. It exists purely because a future negative can flip that “worst” into the best.