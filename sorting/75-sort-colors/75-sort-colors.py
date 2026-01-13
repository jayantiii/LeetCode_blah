class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # single line -->  nums.sort()   --># haha but we need to solve without this.
        
        #idea - 2 pointers ( quicksort) - see notes
        l,r = 0, len(nums)-1
        i = 0
        def swap(i,j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        while i <= r: # condition 
            
            if nums[i] == 0:
                swap(l,i)
                l+=1
            
            elif nums[i] == 2:
                swap(r,i)
                r -=1
                i-=1
            i+=1
        return nums
            
                
        
            
        