class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergesort(nums):
            #Base case
            if len(nums) <= 1:
                return nums

            leftarr = nums[: len(nums)//2]
            rightarr = nums[len(nums)//2:]

            mergesort(leftarr)
            mergesort(rightarr)

            #merge step
            i = 0 #index in left arr
            j = 0 #index in right arr
            k = 0 # index in merged array

            while i < len(leftarr) and j < len(rightarr):
                if leftarr[i] < rightarr[j]:
                    nums[k] = leftarr[i]
                    i+=1
                    k+=1

                else:
                    nums[k] = rightarr[j]
                    j+=1
                    k+=1

            #if left or right arr leftover
            while i < len(leftarr):
                nums[k] = leftarr[i]
                i+=1
                k+=1

            while j < len(rightarr):
                nums[k] = rightarr[j]
                j+=1
                k+=1

            return nums

        return mergesort(nums)




        