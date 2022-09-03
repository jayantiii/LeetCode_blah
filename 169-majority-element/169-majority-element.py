class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #linear time and 0(1) space
        count = {}
        maxcount,res = 0,0
        for n in nums:
            count[n] = count.get(n,0)+1
            res = n if count[n] > maxcount else res
            maxcount = max(count[n],maxcount)
        return res
       








        # #my soln
        # l = len(nums)
        # dic = {}
        # for n in nums:
        #     dic[n] = dic.get(n,0) +1
        # for k,v in dic.items():
        #     if v > l/2:
        #         return k
        
        