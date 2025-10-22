class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        diff = float("inf")
        nums.sort()
        l, r = 0,k -1
        while r <len(nums): # know when it use = and not
            new_diff = nums[r] - nums[l]
            diff = min(diff, new_diff)
            l+=1
            r+=1
            
        return diff

#For the difference between the highest and lowest element to be minimized, the k chosen scores need to be as close to each other as possible.

#What if the array was sorted?
