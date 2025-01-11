class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #use a modified version of bubble sort - 0(n),o(n)
        count = {}
        freq = [[] for i in range (len(nums) + 1)]
        res = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
        for key,val in count.items():
            freq[val].append(key)
        for i in range(len(freq) -1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

    

#one more solution - is to use heap - O(nlogk), O(n+k)

# naive - O(nlogn) , O(n)
#  O(n+n+nlogn+k)=O(nlogn) (sorting dominates)
        # dic = {}
        # res = []
        # for i in range(len(nums)):
        #     dic[nums[i]] = dic.get(nums[i], 0) + 1
        # for key,val in dic.items():
        #     res.append([val,key])
        # res.sort()
        # ans =[]
        # while len(ans) < k:
        #     ans.append(res.pop()[1])
        # return ans


