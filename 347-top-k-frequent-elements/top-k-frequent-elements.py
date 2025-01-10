class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        res = []
        for i in range(len(nums)):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        for key,val in dic.items():
            res.append([val,key])
        res.sort()
        ans =[]
        while len(ans) < k:
            ans.append(res.pop()[1])
        return ans



