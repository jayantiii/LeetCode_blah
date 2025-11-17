class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    #Backtracking, u can make a choice include or not include

        res = []
        def backtrack(index,curr):
            #constraint
            if index == len(nums): #reached the leaf node for that path
                res.append(curr.copy()) # append a copy, cause list in python is by reference
                return

            #Decision 1 - include
            curr.append(nums[index])
            backtrack(index+1,curr) 
            curr.pop() # remove and go to second choice

            #Decision 2 - not include
            backtrack(index+1,curr)

        backtrack(0,[])
        return res

        