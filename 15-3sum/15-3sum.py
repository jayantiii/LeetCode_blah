class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force will have 3 loops. so much more time
        
        #idea - notes
        nums.sort()
        res = []
        for i,n in enumerate(nums):
            if i > 0 and n == nums[i-1]: #--> to avoid duplicate
                continue
            l,r = i+1, len(nums)-1
            
            while l < r:
                sum3 = n + nums[l] + nums[r]
                if sum3 > 0:
                    r -= 1
                elif sum3 < 0:
                    l += 1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l <r:
                        l+=1
                 
        return res
                    
                
        
        