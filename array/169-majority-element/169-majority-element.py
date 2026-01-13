class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #linear time and 0(1) space -- boyer moore algo
        # kinda confusing
        res,count = 0,0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n==res else -1)
        return res
          
            
       
        
       
        # #my soln
        # l = len(nums)
        # dic = {}
        # for n in nums:
        #     dic[n] = dic.get(n,0) +1
        # for k,v in dic.items():
        #     if v > l/2:
        #         return k
        
        
        # another soln
        # count = {} 
        # maxcount,res = 0,0
        # for n in nums:
        #     count[n] = count.get(n,0)+1
        #     res = n if count[n] > maxcount else res
        #     maxcount = max(count[n],maxcount)
        # return res
        