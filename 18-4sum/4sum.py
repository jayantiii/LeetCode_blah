class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)): #4sum
            if i > 0 and nums[i] == nums[i - 1]:   
                continue
            for j in range(i+1,len(nums)): #3sum
                if j > i+1 and nums[j] == nums[j-1]: # j > i+1 this is necessar ok!!
                    continue
                store = set()
                usedpair = set()
                for k in range(j+1,len(nums)): # 2 sum
                    numneeded = target - (nums[i] + nums[j] + nums[k])
                    if numneeded in store:
                        a,b = nums[k], numneeded
                        if a > b:  # so that (2,3) and (3,2) should be considered the same pair
                            a,b = b,a
                        if (a,b) not in usedpair:
                            res.append([nums[i],nums[j],nums[k],numneeded])
                            usedpair.add((a,b))
                    store.add(nums[k])
        return res

# Do NOT skip duplicates for k in this hash-based method like u do for i and j (it can break correctness).
# To prevent duplicate outputs, add a per-(i,j) used_pairs set for the last two values. needed

# You don’t have to use a global seen_quads set for duplicates
# If you (1) sort, (2) skip duplicates for i and j, and (3) dedupe the 2-sum pairs inside each (i,j), then you can avoid duplicates without a global quadruplet set.
    
#---------------2 pointers - sort soln, O(NlogN)+O(N3) ------------------
# You sort the array, then fix two indices (i, j) and solve the remaining 2-sum on the subarray (j+1 .. end) using two pointers k (left) and l (right): if the sum is too small move k++, too big move l--, exact match record and move both.
# All the continue / inner while checks are just duplicate-skips so each value-quadruplet is produced once.       

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         arr = nums
#         n = len(arr)
#         ans = []
#         for i in range(n):
#             if i>0 and arr[i]==arr[i-1]:
#                 continue
#             for j in range(i+1,n):
#                 if j>i+1 and arr[j]==arr[j-1]:
#                     continue
#                 k = j+1
#                 l = n-1
#                 while k<l:
#                     temp = arr[i]+arr[j]+arr[k]+arr[l]
#                     if temp == target:
#                         ans.append([arr[i],arr[j],arr[k],arr[l]])
#                         k+=1
#                         l-=1
#                         while k<l and arr[k]==arr[k-1]:
#                             k+=1
#                         while k<l and arr[l]==arr[l+1]:
#                             l-=1
#                     elif temp<target:
#                         k+=1
#                     else:
#                         l-=1
#         return ans