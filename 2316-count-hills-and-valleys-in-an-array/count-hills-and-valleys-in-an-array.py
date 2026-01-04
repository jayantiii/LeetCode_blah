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
            while left>= 0 and nums[left] == nums[i]: #took more time to frame this
                left-=1
                # dups+=1, #dont calc like duplicate like this, it will count more than

            while right < len(nums) and nums[right] == nums[i]:
                right+=1

            if left < 0 or right >= len(nums): # needed
                continue
            
            if  nums[left] <nums[i] and nums[right] < nums[i]: #then hill
                hills+=1
            if  nums[left] > nums[i] and nums[right] > nums[i]: #then hill
                valleys+=1

        return hills + valleys 

#------------------------Simple clean solnnn----------------------------------------------
# Step 1: remove consecutive duplicates
# Step 2: count local extrema (middle > both neighbors OR middle < both neighbors)
# Warning -> Anything “just count duplicates” will miss monotone/flat patterns and overcount others.

        # a = [nums[0]]
        # for v in nums[1:]:
        #     if v != a[-1]:
        #         a.append(v)

        # ans = 0
        # for i in range(1, len(a) - 1):
        #     if (a[i] > a[i-1] and a[i] > a[i+1]) or (a[i] < a[i-1] and a[i] < a[i+1]):
        #         ans += 1
        # return ans