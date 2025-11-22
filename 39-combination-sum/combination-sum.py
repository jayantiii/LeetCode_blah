class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, subset, currsum):
            if i == len(candidates):
                if currsum == target:
                    res.append(subset.copy())
                return #dont forget
            if currsum > target:
                return
            
            #include, do i cause can repeat
            backtrack(i, subset + [candidates[i]], currsum + candidates[i] )

            #not include
            backtrack(i+1, subset,currsum)


        backtrack(0, [],0)
        return res

# candidates = [2,3,5], target = 8

# backtrack(0, [], 0)

#   backtrack(0, [2], 2)
  
#     backtrack(0, [2,2], 4)
    
#       backtrack(0, [2,2,2], 6)
      
#         backtrack(0, [2,2,2,2], 8)  ✓ hit target
        
#         backtrack(1, [2,2,2], 6)
#           backtrack(1, [2,2,2,3], 9)
#           backtrack(2, [2,2,2], 6)
#             backtrack(2, [2,2,2,5], 11)
#             backtrack(3, [2,2,2], 6)
      
#       backtrack(1, [2,2], 4)
#         backtrack(1, [2,2,3], 7)
#           backtrack(1, [2,2,3,3], 10)
#           backtrack(2, [2,2,3], 7)
#             backtrack(2, [2,2,3,5], 12)
#             backtrack(3, [2,2,3], 7)
        
#         backtrack(2, [2,2], 4)
#           backtrack(2, [2,2,5], 9)
#           backtrack(3, [2,2], 4)
    
#     backtrack(1, [2], 2)
#       backtrack(1, [2,3], 5)
#         backtrack(1, [2,3,3], 8)   ✓ hit target
        
#         backtrack(2, [2,3], 5)
#           backtrack(2, [2,3,5], 10)
#           backtrack(3, [2,3], 5)
      
#       backtrack(2, [2], 2)
#         backtrack(2, [2,5], 7)
#           backtrack(2, [2,5,5], 12)
#           backtrack(3, [2,5], 7)
        
#         backtrack(3, [2], 2)
  
#   backtrack(1, [], 0)
#     backtrack(1, [3], 3)
#       backtrack(1, [3,3], 6)
#         backtrack(1, [3,3,3], 9)
#         backtrack(2, [3,3], 6)
#           backtrack(2, [3,3,5], 11)
#           backtrack(3, [3,3], 6)
      
#       backtrack(2, [3], 3)
#         backtrack(2, [3,5], 8)   ✓ hit target
        
#         backtrack(3, [3], 3)
    
#     backtrack(2, [], 0)
#       backtrack(2, [5], 5)
#         backtrack(2, [5,5], 10)
#         backtrack(3, [5], 5)

#     backtrack(3, [], 0)


# #✔ Combination Sum (unlimited reuse allowed)
# AND #Combinations (each number used once, strictly increasing)
# This determines whether you use a for loop or two recursive branche





#example of backtrack
#                           dfs(0, [])
#                 /                                \
#          exclude 1                         include 1
#          dfs(1, [])                        dfs(1, [1])
#          /        \                        /          \
#  exclude 2   include 2             exclude 2      include 2
# dfs(2,[])   dfs(2,[2])            dfs(2,[1])     dfs(2,[1,2])

#Yes, exactly: every subset you append is at a leaf node of the recursion tree.

#Brute force code to find all subsets problem!! This wont for this cause
# That’s fine for power set, but for combination sum we must: allow repeating the same candidate

#def all_subsets_loop(nums):
    # result = [[]]   # start with empty subset
    
    # for x in nums:
    #     new_subsets = []
    #     for subset in result:
    #         new_subset = subset + [x]  # copy + include x
    #         new_subsets.append(new_subset)
    #     result.extend(new_subsets)

    # return result


        