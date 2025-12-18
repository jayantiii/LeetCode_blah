class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        m = min(nums)
        expected = set(range(m,len(nums)+m)) #Ooooo
        for n in nums:
            if n in expected:
                expected.remove(n)
            else:
                return False

        return len(expected) == 0

#Sn = n(a + alast)/2

#My answer!! works but fails the TC - nums = [0,3,0,3]
#    nums.sort()
#         n = len(nums)
#         expectedalast = nums[0] + n -1
#         expectedsum = n *(nums[0] + expectedalast ) //2
#         return sum(nums) ==  expectedsum

        