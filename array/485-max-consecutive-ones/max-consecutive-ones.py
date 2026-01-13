class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        currcount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currcount+=1
            else:
                currcount = 0
            maxcount = max(currcount,maxcount) #dont do this inside else
            #if did this in else, it will not run and when the array ends with 1, so one last 1 count be missed

        return maxcount
        
# maxcount = max(currcount,maxcount), DONT DO THIS INSIDE LOOP
#the last loop it gets skipped orelse, I keep doing simlar mistakes, did this in google interview too, interviewer pointed it