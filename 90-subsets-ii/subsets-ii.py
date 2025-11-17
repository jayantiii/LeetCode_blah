class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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
            while i+1< len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1,curr)

        backtrack(0,[])

        return res
        