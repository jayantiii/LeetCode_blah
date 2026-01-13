class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = []
    # Use in-place marking to get O(n) time
        for i in range(len(nums)):
            x = abs(nums[i])
            nums[x-1] = -(abs(nums[x-1]))
            #abs is necessary cause a value can repeat dont forget!!
        
        for i in range(len(nums)):
            if nums[i] > 0:
                arr.append(i+1)
        return arr


# ## TLE         
#   arr = []
#         for i in range(1,len(nums)+1):
#             if i not in nums:
#                 arr.append(i)
#         return arr

# The key insight is: if a number x exists in the array, we can mark its corresponding index x-1 as visited by making it negative. At the end, any index that is still positive means its number (index + 1) is missing.