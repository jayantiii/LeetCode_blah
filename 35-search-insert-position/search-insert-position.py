class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #user binary search, log(n)
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid-1
            else:
                return mid #equal
        # understand the logic, we dont need extra var par, just can return l
        return l

# this works but its O(n)
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        #     if nums[i] > target:
        #         return i

        # return i+1 #this should be i+1 in case all nums are less than target

        