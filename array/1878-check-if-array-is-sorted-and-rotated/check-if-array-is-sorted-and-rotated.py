class Solution:
    def check(self, nums: List[int]) -> bool:
        prev = nums[0]
        pivot = -1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]: #not sorted
                pivot = i
                break #IMP->break at first pivot

        # If no pivot was found, the array is already sorted
        if pivot == -1:return True

        for i in range(pivot+1, len(nums)): #ensure there is no other pivot
            if nums[i-1] > nums[i]:
                return False

        # The last element must be <= the first element
        return nums[-1] <= nums[0]

#----------------Clean Better SOLN------------------------
        # count = 0
        # n = len(nums)
        
        # for i in range(n):
        #     # Use modulo to check the last element against the first
        #     if nums[i] > nums[(i + 1) % n]:
        #         count += 1
        
        # # If there is more than 1 break, it's not a rotated sorted array
        # return count <= 1

# In a rotated non-decreasing array, you see that violation exactly once:
# at the rotation boundary.

# Using (i+1) % n checks the wrap-around pair last -> first, which 
#is mandatory to validate rotation.


        
        