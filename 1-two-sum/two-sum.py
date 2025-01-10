class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in dic:
                return [i, dic[a]]
            dic[nums[i]] = i


# this passes only 2 cases
# for i in range(len(nums)):
#             a = target - nums[i]
#             if a in nums and nums[i]!=a:   --- logic issue when nums = [3,3]
#                 return [i, nums.index(a)]