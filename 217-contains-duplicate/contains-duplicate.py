class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #tc and sc = 0(n)
        if len(set(nums)) != len(nums):
            return True
        else:
            return False

#return len(set(nums)) < len(nums)

#or can use hashset too
    #  seen = set()
    #     for num in nums:
    #         if num in seen:
    #             return True
    #         seen.add(num)
    #     return False
        