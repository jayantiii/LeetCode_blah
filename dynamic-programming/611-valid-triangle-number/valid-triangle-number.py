class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #O(n² log n)
        n = len(nums)
        nums.sort()
        count = 0
        #choose nums[i] + nums[j] > nums[k]
        for i in range(len(nums)-2):#see the bounds
            for j in range(i+1,len(nums)-1):
                twosides = nums[i] + nums[j]
                # first index k where nums[k] >= twosides (so nums[j+1 : k] are valid)
                index = bisect_left(nums, twosides, j + 1, n) #syntax
                count = count +  index -(j +1) #formula understand
        return count



# Sort the array first, then use binary search to find the third value of a triangle.
# Valid Triangle means if you added length of any 2 side it will be greater than 3rd side length

#------How tp get count formula-----------
# Valid third sides are k in [j+1, index-1] (since index is first k with nums[k] >= nums[i]+nums[j]),
# so count added is (index-1) - (j+1) + 1 = index - (j+1).
# Count of integers in inclusive range [L, R] is: R - L + 1

#-------------Mymistake------------
#bisect_left(nums[j:], twosides) is wrong , cant do this cause index is relative to slice not original list
#also line12-index is the first position where the triangle fails not passes!!! dont confuse it

#--------------Optimal solution 2 POINTERS , O(n2)!-----------------------------
# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         count = 0

#         for k in range(2, n):          # nums[k] is the largest side
#             i, j = 0, k - 1
#             while i < j:
#                 if nums[i] + nums[j] > nums[k]:
#                     count += (j - i)   # all pairs (i..j-1, j) work
#                     j -= 1
#                 else:
#                     i += 1
#         return count
