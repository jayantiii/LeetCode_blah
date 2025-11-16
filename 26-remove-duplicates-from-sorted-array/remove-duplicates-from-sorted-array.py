class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # write always moves slower than read.
        # write  marks the position where the next unique value should be written
        # read is scanning all positions (0,1,2,...,n-1)
        # Goal is nums[0 : write+1] is duplicate-free
        write = 0
        for read in range(1, len(nums)):
            #Found new num, we must place it after the last unique number:
            if nums[write] != nums[read]: 
                write +=1  # is needed
                nums[write] = nums[read]

        return write + 1 # plus 1 cause we are returning count











#My first try - had problems!
# mutating (pop) the list while iterating forward over it. That makes indices shift and you skip elements (or can hit index errors). 

#         curr = nums[0]
#         for i in range(1,len(nums)):
#             if nums[i] == curr:
#                 nums.pop(i)
#             else:
#                 curr = nums[i]
#         return nums
        