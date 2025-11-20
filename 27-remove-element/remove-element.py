class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
      #idea  #We can move all the occurrences of this element to the end of the array. Use two pointers!
#The order of the elements may be changed. Imp point

        write = len(nums) -1
        for i in range(len(nums)):
            #Also, need a condition for checking if i < write
            # if i>write:
            #     break
            #But what if the next element at the new write index is also val
            #so dont do only if, do a while
            while i <= write and nums[write] == val:  #condition
                write -=1
            #Also, need a condition for checking if i < write
            if i>write:
                break

            if nums[i] == val:
                nums[i] = nums[write]
                nums[write] = val
                write -=1  

        return write +1


        