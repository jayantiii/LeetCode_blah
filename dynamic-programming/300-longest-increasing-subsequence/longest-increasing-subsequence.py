class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #DP
        lis = [1]*len(nums) #cause default is 1! LIS ending at i is at least 1
        for i in range(1,len(nums)):
           j = i-1    
           maxlength = 1 #start at 1, LIS ending at i is at least 1
           while j >=0:
            if nums[i] > nums[j]:
                length = 1+lis[j]
                maxlength = max(maxlength, length)
            lis[i] =  maxlength
            j-=1
        return max(lis)


#You need to compare nums[i] with all previous j < i: need 2 loops!
#To find LIS ending at index i, you must check ALL previous indices j < i. IMP to understand!!
#lis[i] = longest increasing subsequence that ends exactly at index i
# lis[i] = 1 + max( lis[j] )  
#           for all j < i  
#           where nums[j] < nums[i]

#More Better !! optimised T - o(nlogn) soln
#We maintain an array tails where tails[k] is the minimum ending value of an increasing subsequence of length k+1. For each number,we binary search its position in tails. This yields O(n log n).

    # def lengthOfLIS(self, nums):
    #     tails = []

    #     for num in nums:
    #         pos = bisect_left(tails, num)

    #         if pos == len(tails):
    #             tails.append(num)       # extend LIS
    #         else:
    #             tails[pos] = num        # optimize tail

    #     return len(tails)

#DFS SOLN, TLE
#WITHOUT MEMO, 2 to pwer n
#For LIS, the decision at index i depends on what previous value you picked, not on “maxlen so far”.
        #Time Complexity = O(n²), Space Complexity = O(n²) (memo), Recursion depth = O(n)
        # @lru_cache(None) #use this lien for memo
        # def dfs(i,previndex):
        #     if i == len(nums):
        #         return 0             
        #     # Option 1: skip nums[i]
        #     skip = dfs(i+1, previndex)
        #     # Option 2: take nums[i] if it is strictly increasing
        #     include = 0 # If you don’t initialize include, you will get error
        #     if previndex == -1 or nums[i] > nums[previndex]:
        #         include = 1+ dfs(i+1, i)

        #     return max(skip,include)
        # return dfs(0,-1)


# nums[3,10,2]
#                                       dfs(0, prev = -∞)
#                               /                                   \
#                         Skip 3                                     Take 3
#                    dfs(1, -∞)                                  dfs(1, 3)
#               /                  \                        /                    \
#          Skip 10                Take 10             Skip 10                   Take 10
#      dfs(2, -∞)            dfs(2, 10)            dfs(2, 3)                 dfs(2, 10)
#       /      \              /      \             /       \                 /       \
#  Skip 2    Take 2     Skip 2   Take 2(X)   Skip 2    Take 2(X)        Skip 2    Take 2(X)
# dfs(3,-∞)  dfs(3,2)   dfs(3,10)    X       dfs(3,3)     X           dfs(3,10)       X
#    0          1          0                    0                        0

        