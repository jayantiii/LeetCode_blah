# Method 1 -- Apply hashtable O(n)
# hashNum = {}     --dict
# for i in nums:
#     if i not in hashNum:
#         hashNum[i] = 1
#     else:
#         return True
# return False
**# Method 2 -- Sorting**
# l =  len(nums)
# if l < 2:
#     return False
# nums.sort()
# for i in range(l-1):                    ---- (l-1)
#     if nums[i] == nums[i+1]:
#         return True
# return False