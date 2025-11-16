class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #user binary search
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] < target:
                l = mid +1
                pos = l
            elif nums[mid] > target:
                r = mid-1
                pos= r
            else:
                return mid #equal

        return l

# this works but its O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     if nums[i] > target:
        #         return i

        # return i+1 #this should be i+1 in case all nums are less than target

        