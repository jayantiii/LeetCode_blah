class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        #IMP - see how this works!!
        def isvalid(cap):
            count, i = 0,0
            while i <len(nums):
                if nums[i] <= cap:
                    count+=1
                    i+=2
                else:
                    i+=1

            return count >= k

        # #Binary search the range of answers
        l,r = min(nums), max(nums)
        while l<=r:
            mid = (l+r)//2

            if isvalid(mid): #if valid capability
                r=mid-1
            else:
                l = mid +1

        return l

## Normally, if a question asks for the 'maximum of some minimum' or 'minimum of some maximum' it can be solved using Binary Search.

## Capability cap = 3 means: every robbed house must have value ≤ 3 (equivalently, the max robbed value is ≤ 3). You are not required to rob a house with value exactly 3.   

# There are 3 layers to crack this problem --:

# Understand that DP will fail since number of states is quadratic.
# Think of binary search approach since its min-max.
# Realise that we can greedily check if a given capability is possible and based on it, shrink the search space for binary search.

#--------------------Backtracking---------------------------------------
# backtrack(i, t) returns the minimum possible capability (smallest max robbed value) to pick exactly t non-adjacent houses from nums[i:].

        # def backtrack(i,k):
        #     if k == 0: #picked k houses
        #         return 0

        #     if i>= len(nums): # impossible to pick the required number of houses.
        #         return float("inf") #Invalid path

        #     #skip
        #     skip = backtrack(i+1,k)

        #     #take
        #     take = max(nums[i], backtrack(i+2,k -1))     #i+2

        #     return min(skip,take)

        # return backtrack(0,k)

#----------Example  to understand why  return float("inf") ---
# [5] , k = 1

# backtrack(0,1)
#   skip = backtrack(1,1)
#          i=1 >= n=1  AND need=1 -> return inf   

#   take = max(nums[0]=5, backtrack(2,0))
#          backtrack(2,0): need=0 -> return 0
#          take = max(5,0) = 5

#   answer = min(skip=inf, take=5) = 5          


##---------Why no 1D dp----------------------------------
# dp[i] -> minimum capability using houses 1..i is not enough state.

# Because the answer depends on (a) how many houses you robbed so far and (b) whether you robbed the previous house (adjacency constraint). Without those, dp[i] can’t tell what choices are still legal.