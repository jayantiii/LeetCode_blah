class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        dic = {}
        for n in nums:
            dic[n] = dic.get(n,0) +1
        for k,v in dic.items():
            if v > l/2:
                return k
        
        