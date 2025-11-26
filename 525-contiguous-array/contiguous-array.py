class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen = 0
        prefixsum = {} #store, sum: index
        prefixsum[0] = -1 #So that a subarray starting at index 0 is counted.
        currsum = 0
        for i in range(len(nums)):
            num = 1 if nums[i] == 1 else -1
            currsum += num
            if currsum in prefixsum: #means that sum has been seen before
                index = prefixsum[currsum]
                subarraysize = i - index
                maxlen = max(maxlen, subarraysize)

            #store prefix sum
            if currsum not in prefixsum:
                prefixsum[currsum] = i
        return maxlen


        
#n2 subarray for n elements
#cant use sliding window, cause its not possible to make a guarranted decision of when to shrink

#Idea,Interesting!!!
# - turn all 0 to -1s
# - we are trying to find longest subarray of sum zero, Now equal 0s and 1s means the subarray sum = 0.
# - Maintain a hashmap storing the first index where each prefix sum appears.
# - If the prefix sum repeats at index j (first seen at i), then the subarray (i+1 … j) has sum 0 → equal 0s and 1s.
# - Initialize prefix sum 0 at index –1 so segments starting at index 0 are counted.

#Try to visualise, increase when +1, decrease when -1
# If the prefix sum ever returns to a value you’ve seen before, it means everything between those two positions canceled out to zero.