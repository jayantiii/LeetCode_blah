class Solution:         
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #skip same number
                continue
            first = nums[i]
            remain =  -1* first

            l,r = i+1, len(nums) -1
            while l<r:
                if nums[l]+nums[r] > remain:
                    r-=1
                elif nums[l] + nums[r] < remain:
                    l+=1
                else:
                    res.append([first, nums[l],nums[r]])
                    l+=1
                    while l < r and nums[l]==nums[l-1]:
                        l+=1

        return res






#dont contain triplets! 