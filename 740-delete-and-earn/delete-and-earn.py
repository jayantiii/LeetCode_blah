class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #Main key - dp over the unique values and have a count hashmap!!
        count = Counter(nums)
        values = sorted(count) #  # unique values

        m = len(values)
        dp = [0] * m
        dp[0] = count[values[0]] *values[0]

        for i in range(1,m):
                
            skip = dp[i-1]

            #take
            earn = count[values[i]] *values[i]

            if values[i] == values[i-1] + 1: #if conflict
                take = earn + (dp[i-2] if i >= 2 else 0)
            else:
                take = earn + dp[i-1]
            
            dp[i] = max(skip,take)

        return dp[-1]

# dp[i] means:
# Maximum points you can earn using only the first i+1 unique values (i.e., values vals[0..i]).
            
#Stop mixing raw-index DP with value-count DP. Once you do count = Counter(nums), your DP must run over unique values, not len(nums).


#         nums.sort() #since order of picking not matter but value

#         @lru_cache(None)
#         def backtrack(i):
#             if i == len(nums):
#                 return 0
         
#             #skip
#             skip = backtrack(i+1)


#             #pick 
#             j = i
#             count = 0

#             ##Pick all of the same value nums[i]
#             while j < len(nums):
#                 if nums[j] ==nums[i]:
#                     count+=1
#                     j+=1
#                 else: break

#             ## next backtrack to value more than nums[i] + 1
#             k = j
#             while k < len(nums):
#                 if nums[k] == nums[i] +1:
#                     k+=1
#                 else: break

#             pick = count*nums[i] + backtrack(k)

#             return max(skip,pick)


#         return backtrack(0)

# # We compute backtrack(i) for every index i (≈ n states), and each state may scan forward with j/k (up to ≈ n steps).
# # Those repeated forward scans across many i re-check the same elements, so worst-case work adds up to
# #-->  O(n^2).



        