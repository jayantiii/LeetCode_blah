class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        used = [False] * len(nums)
        def backtrack(subset): #i not needed
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
      
            for j in range(len(nums)): #pick choose
                if used[j]:
                    continue

                # CONFUSING --> duplicate-skip:
                # if same value as previous,taking nums[j] would create a duplicate
                # So we do not start a second root branch with the “second SAME”.
                if j > 0 and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue

                subset.append(nums[j])
                used[j] = True

                backtrack(subset) #next element

                subset.pop() #IMP - remove!
                used[j] = False  #IMP - unset!

        backtrack([])
        return res

# To handle duplicates in Permutations II, the trick is: sort first, then skip picking the same value at the same recursion “level” unless the previous identical one was used.

# Mental model
# Each recursion call = “I have built subset of length k. Now choose the (k+1)-th element.”
# The for loop enumerates all possible choices for that next element (subject to used[] + duplicate-skip).

#backtrack([])
# ├── pick 1a (j=0)        -> backtrack([1])
# │   ├── pick 1b (j=1)    -> backtrack([1,1])
# │   │   └── pick 2 (j=2) -> backtrack([1,1,2])  ✅ output
# │   └── pick 2 (j=2)     -> backtrack([1,2])
# │       └── pick 1b (j=1)-> backtrack([1,2,1])  ✅ output
# ├── pick 1b (j=1)        -> ❌ SKIPPED (duplicate-skip rule)
# └── pick 2 (j=2)         -> backtrack([2])
#     ├── pick 1a (j=0)    -> backtrack([2,1])
#     │   └── pick 1b (j=1)-> backtrack([2,1,1])  ✅ output
#     └── pick 1b (j=1)    -> ❌ SKIPPED (duplicate-skip rule)

#----------Better way no sort - use hashmap count-----------------------------------
        # cnt = Counter(nums)
        # n = len(nums)
        # res: List[List[int]] = []
        # path: List[int] = []

        # def dfs() -> None:
        #     if len(path) == n:
        #         res.append(path.copy())
        #         return
        #     for v in cnt:
        #         if cnt[v] == 0:
        #             continue
        #         cnt[v] -= 1
        #         path.append(v)
        #         dfs()
        #         path.pop()
        #         cnt[v] += 1

        # dfs()
        # return res

#----- confusing skip dup rule--------------------------------------
 #Rule enforced here:
#   "You can only pick the later duplicate (j) if the earlier duplicate (j-1)
#    has already been picked somewhere earlier in the CURRENT path."
#
# That is exactly what `not used[j-1]` checks.
#
# If used[j-1] == False:
#   earlier copy isn't in the path, so picking the later copy first would create
#   a duplicate branch -> SKIP.
#
# If used[j-1] == True:
#   earlier copy is already in the path, so picking this later copy is the
#   correct way to place duplicates (e.g., building [1,1,2]) -> ALLOW.
