class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Modified Bineary search

        l,r = 0, len(nums) -1
        while l<=r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: #left sorted part
                if nums[l] <=  target < nums[mid]:
                    r = mid -1
                else:
                    l = mid +1

            else: #right sorted part
                if  nums[mid] < target<= nums[r]:
                    l =mid +1
                else:
                    r = mid -1

        return -1
        