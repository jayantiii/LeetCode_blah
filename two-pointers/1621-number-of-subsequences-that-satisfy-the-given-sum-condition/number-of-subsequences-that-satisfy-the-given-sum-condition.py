class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        ## Persistent pointer - starts at the end and never resets
        right = len(nums) -1
        for i in range(len(nums)):
            while i<=right and nums[i] + nums[right] > target:
                right -=1
            count = right-i 
            #total subsequence with nums[i] as minimum
            
            if i <= right:
                total+= 2** count

        return total % (10**9 + 7)

        
        








#@Use two pointers approach: Given an index i (choose it as the minimum in a subsequence) find the maximum j where j ≥ i and nums[i] +nums[j] ≤ target.

#Understand this very clearly, dont try to make it 0(n2) by resetting right pointer every time

# 1. Sort the array so that for any window, the first element is the min  and the last element is the max. Order doesn't matter for subsequences.

# 2. Use two pointers: 'i' moves from left to right (current minimum),   and 'right' starts at the end and only moves left (current maximum).

# 3. For each 'i', move 'right' left until the sum (nums[i] + nums[right]) 
#    is less than or equal to the target.

# 4. Because the array is sorted, if a value at 'right' was too big for 
#    the previous 'i', it is definitely too big for this 'i'. 
#    Never reset 'right' to the end; this keeps the logic O(n).

# 5. If the window is valid (i <= right), then nums[i] MUST be included 
#    to be the minimum. Every other element in the range [i+1...right] 
#    is optional (can be in or out).

# 6. The number of optional elements is (right - i).
#    Since each optional element has 2 choices, add 2^(right - i) to the total.

# -----------------------------------------------

#Backtrack 2n way! TLE
        # def numsub(i,minn,maxx):
        #     if i == len(nums):
        #         if maxx + minn <= target:
        #             return 1
        #         else:
        #             return 0

        #     #skip
        #     skip = numsub(i+1,minn,maxx)

        #     #Take # TAKE: Pass the NEW minn/maxx without overwriting the current ones!! dont write minn,maxx
        #     newminn = min(minn,nums[i])
        #     newmaxx = max(maxx,nums[i])
        #     take = numsub(i+1,newminn,newmaxx)

        #     return skip + take

        # return numsub(0,float("inf"),float("-inf")) 

##----------- 0(N) CLEANER APPROACH ====------------------
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         left = 0
#         right = n - 1
#         total = 0
#         mod = 10**9 + 7
        
#         while left <= right:
#             # Check if the smallest + largest in our current window is okay
#             if nums[left] + nums[right] <= target:
#                 # We found a valid range! 
#                 # All subsequences starting with nums[left] are valid.
#                 # The number of choices is (right - left)
#                 total += pow(2, right - left, mod)
                
#                 # Move left to check the next possible minimum
#                 left += 1
#             else:
#                 # Sum is too big, so the current nums[right] 
#                 # cannot be the maximum for nums[left].
#                 right -= 1
                
#         return total % mod

#-------------------------------
#Explanation for why sorting is okay in this problem with subsequences:

# The use of the term subsequence here sort of confused me at first. Basically, to get an optimal solution, most people use sorting. At first I was confused since it seemed like sorting would mess up the order and we care about subsequences, not combinations. In most subsequence problems you don't change the order of the original array.

# But basically, since we only care about minimum and maximum, we can pick and choose to include whatever we want and treat it as a subsequence. So its basically asking how many different combinations of numbers exist within nums such that it satisfies the given condition. The fact that they are asking for subsequences only affects the order of how the numbers are ordered in the combination, not the combination itself.

# --------------------

#Note - If you are struggling in these types of Questions, practice more of Questions on Sorting + Greedy + Counting, and make a template of your own. Finally you will begin to recognise the pattern.

