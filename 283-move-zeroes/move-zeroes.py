class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """              
        # nums = [0,1,0,3,12]
        #           w.  r
        #        [1,0,0,3,12]
        #             w r
        #        [1,3,0,0,12]


        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                temp = nums[write]
                nums[write] = nums[read]
                nums[read] = temp
                write+=1        
                #write = read  - this is wrong, This makes write jump ahead to the same position as read.
# Then both pointers move together, preventing the correct compaction of non-zero elements.
        return nums



        