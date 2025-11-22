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
            
            #include
            backtrack(i, subset + [candidates[i]], currsum + candidates[i] )
            backtrack(i+1, subset,currsum)


        backtrack(0, [],0)
        return res









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


        