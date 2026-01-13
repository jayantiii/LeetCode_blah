class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #nums.sort() # this dont return anything
        # But after sorting how will u keep track of indexes
        # soln lil like 2 sum
        res = []
        temp = sorted(nums)
        dic ={}
        for i, x in enumerate(temp):
            if x not in dic:
                dic[x] = i

        for i in nums:
            res.append(dic[i])
        
        return res
            


        