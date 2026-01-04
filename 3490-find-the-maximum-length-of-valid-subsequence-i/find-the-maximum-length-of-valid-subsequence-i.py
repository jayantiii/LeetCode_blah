from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # Patterns 1 & 2: all even or all odd
        evens = sum((x & 1) == 0 for x in nums)
        odds = len(nums) - evens
        best_same = max(evens, odds)

        # Patterns 3 & 4: alternating parity
        end_even = 0  # best alternating subseq ending with even
        end_odd = 0   # best alternating subseq ending with odd

        for x in nums:
            if x & 1:  # odd, x & 1 = 1, bitwise AND. It’s a fast way to check if x is odd.
                end_odd = max(end_odd, end_even + 1) 
                #IMP -> If you want an alternating that ends with odd, the element right before it  must be even
                
            else: # even, x & 1 = 0
                end_even = max(end_even, end_odd + 1) # Symmetric. To end with even, previous must be odd:

        return max(best_same, end_even, end_odd)


#Observations!!
# k can either be 1 or be 0 only, nothing else --- IMPPPP
# That’s the key: the “best length” ending at i is not enough information. You need “best length ending at i for each k”.
# Use two DP states per index:
# dp0[i] = best length ending at i with k=0
# dp1[i] = best length ending at i with k=1    

# Greedy will work here, #DP is for OVERLAPPING problems, 
# (1) %2 means checking whether number is even or odd.
# (2) Hence the entire questions is built on concept :
# (a) Even + Even = Even
# (b) Odd + Odd = Even
# (c) Even + Odd = Odd
# (d) Odd + Even = Odd

#Based on above--------------
# Greedy comes from the fact that validity depends only on parity pattern, and there are only 4 possible patterns:
# E E E E ... (all even)
# O O O O ... (all odd)
# E O E O ... (alternating starting even)
# O E O E ... (alternating starting odd)
# So “find longest valid subsequence” = “take the max length among these 4”.

### --------------------DP INTERESTING GOOD solution - TLE-----------------------------------------------
    # def maximumLength(self, nums: List[int]) -> int:
    #     #dp[i], longest valid subsequence that ends at i!!better!!
    #     if len(nums) == 1:
    #         return 1

    #     dpeven= [1 for i in range(len(nums))]  #initialise as 1!! not zero
    #     dpodd= [1 for i in range(len(nums))] 
        
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             if (nums[i] + nums[j]) % 2 == 0:
    #                 dpeven[i] = max(dpeven[i], dpeven[j]+1)
    #             elif (nums[i] + nums[j]) % 2 == 1:
    #                 dpodd[i] = max(dpodd[i],dpodd[j] +1)
       
    #     return max(max(dpeven), max(dpodd))

##-----------------------------------------My mistake while DP---MAJ0R---------------------------
#I had one dp array and one calc array to store the equation value for longest ending at i!! VERY BAD

# Why one calc[i] is not enough
# “for the best subsequence ending at index i, what is its k (0 or 1)?”
# Even if one is slightly shorter right now, it can be the only one that can be extended later to become the global best. If you store only one calc[i], you delete the other possibility permanently.

# Why “future” matters
# Two subsequences can both end at the same index i, but have different k. Even if they have the same length (or one is slightly shorter), they can have different ability to extend with future numbers.
# So one does not dominate the other.

# Because “taking max” only works when the shorter option can never beat the longer option in the future (i.e., the longer one dominates it). Here, a longer subsequence ending at i can be worse than a shorter one ending at i, because they enforce different constraints on what you’re allowed to append next.

#--------------------Example to show why it fails---------------------------------------------------------------
# Why dp[i] + calc[i] (single k) fails:
# For any valid subsequence, ALL adjacent-pair sums have the SAME parity:
#     k = (sub[t] + sub[t+1]) % 2   for every t
# So every valid subsequence "chooses" one fixed k:
#     k = 0  -> every adjacent sum even
#     k = 1  -> every adjacent sum odd
#
# IMPORTANT: At the same end index i, you can have TWO different best candidates:
#   - best subsequence ending at i with k=0
#   - best subsequence ending at i with k=1
#
# A single calc[i] can store only one k, so it may discard the other candidate.
# But the discarded one might be the ONLY one that can be extended later.
#
# Example nums = [2, 1, 4, 3]
# i=2 (value 4):
#   [2,4] has k = (2+4)%2 = 0, length 2
#   [1,4] has k = (1+4)%2 = 1, length 2
# If calc[2] stores only 0 (picked [2,4]),
# then at i=3 (value 3):
#   (4+3)%2 = 1, so ONLY the k=1 subsequence can extend -> [1,4,3] length 3
#   the k=0 subsequence cannot extend.
# If you discarded k=1 at i=2, you miss the optimal answer.
#
# Therefore dp must be split by k:
#   dp[i][0] = best length ending at i with k=0
#   dp[i][1] = best length ending at i with k=1
#
# This keeps both "modes" alive for future extensions.