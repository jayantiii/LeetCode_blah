class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #whenever duplicate q, think about sets

        res = []
        set_nums = set(nums)

        for i in range(1, len(nums) +1):
            if i not in set_nums:
                res.append(i) # this is wrong - res.append[i]

        return res

        