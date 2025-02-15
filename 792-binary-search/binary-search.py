class Solution:
    def search(self, nums: List[int], target: int) -> int:
# so basically, use l and r and find mid each iteration
        l, r = 0, len(nums) - 1 #dont forget -1 for r, and l is o not 1
        while l <=r:
            mid = (l + r )// 2   ## dont forget the brackets
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
        return -1

        