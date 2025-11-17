class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #T - O(n · 2ⁿ)
        res = []
        nums.sort() # nlogn

        def backtrack(i, curr):
            #constraint
            if i == len(nums):
                res.append(curr.copy())
                return # necessary

            #decision1 , include nums[i]
            curr.append(nums[i])
            backtrack(i+1,curr)
            curr.pop()

            #decision2, all subsets thatbnot include nums[i]

            #After you choose not to take nums[i],you skip equal elements(nums[i+1]...)
            # If we are not including nums[i], it means we dont include any num of that value
            #Thus, we skip the the indexs that have value nums[i], thus we sort nums before
            while i+1< len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1,curr)

        backtrack(0,[])

        return res


# Brute force:
# Generate all 2^n subsets as if all elements were distinct.
# Normalize each subset (e.g., treat it as a tuple).
# Use a set to remove duplicates.
# Convert back to list of lists.
        