class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in range(len(nums)): # dont forget len()
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos+=1

        for i in range(pos, len(nums)):
            nums[i] = 0

   




#lot of index errors
    #  zero = 0
    #     for i, x in enumerate(nums):
    #          #enumerate(nums) uses the list's original length and static index range.
    #         if x == 0:
    #         # wrong - nums.pop(i) inside a loop over enumerate(nums), index shifting
    #             zero +=1
        
    #     # nums = nums + [0]*zero
    #     l = len(nums)
    #     for i in range(zero):
    #         nums[i+l] = 0
    #     return nums


        