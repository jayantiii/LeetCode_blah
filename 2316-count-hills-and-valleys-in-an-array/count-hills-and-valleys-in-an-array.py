class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hills = 0
        valleys = 0
        # no need to take first and last index, as it not both
        for i in range(1,len(nums)-1): 
            if nums[i] == nums[i-1]: #good way to skip duplicates
                continue 

            left = i-1
            right = i+1
            while left>= 0 and nums[left] == nums[i]:
                left-=1
                # dups+=1, #dont calc like duplicate like this, it will count more than

            while right < len(nums) and nums[right] == nums[i]:
                right+=1

            if left < 0 or right >= len(nums):
                continue
            
            if  nums[left] <nums[i] and nums[right] < nums[i]: #then hill
                hills+=1
            if  nums[left] > nums[i] and nums[right] > nums[i]: #then hill
                valleys+=1

        return hills + valleys 
            
#non equal niehbour means - not equal to itsself 
#[ 2,3,3,3,5,6]