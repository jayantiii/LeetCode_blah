class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boores method?
        maj = nums[0]
        c =1
        for i in range(1,len(nums)):
            if nums[i] == maj:
                c += 1
            else:
                if c <= 0:
                    maj = nums[i]
                else:
                    c = c -1 
        return maj



        