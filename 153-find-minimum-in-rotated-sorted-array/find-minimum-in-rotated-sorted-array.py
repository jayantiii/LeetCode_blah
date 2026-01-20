class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l< r: ##if u do equal sign here, then forever loop!
            mid = (l+r)//2

            if nums[mid] > nums[r]: #go right
                l  = mid + 1
            else: #go left
                r = mid ##keep mid cause, mid can also be the minimum.

        return nums[l]

            
#--------------------------My mistakesss--------------
#I wrote some complex condn like below
# You can’t “minimally fix” your two-branch idea (using both nums[l] and nums[r] with strict inequalities) because it’s logically unstable in a rotated array: the ends don’t form a monotonic frame.

#  if nums[mid] > nums[l] and nums[mid]<nums[r]: #go left
#                 r  = mid - 1
            
# elif nums[mid] < nums[l] and nums[mid] > nums[r]: #go right
#                 l = mid +1
        
##---------Why return nums[l]---------------------------------
# In the correct binary search, you maintain this invariant:
# The minimum element is always inside the current search window [l, r].
# And you shrink the window until only one index remains. When the loop ends, you have:
# l == r
# so the only possible location of the minimum is that index
# therefore the answer is nums[l] (same as nums[r]).
# That’s why returning nums[l] is correct: at termination, l is the index of the minimum.