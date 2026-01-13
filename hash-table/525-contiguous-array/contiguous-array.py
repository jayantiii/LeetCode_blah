class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlen = 0
        prefixsum = {} #store, sum: index
        prefixsum[0] = -1 #IMPP- So that a subarray starting at index 0 is counted.
        currsum = 0
        for i in range(len(nums)):
            num = 1 if nums[i] == 1 else -1
            currsum += num
            if currsum in prefixsum: #means that sum has been seen before
                index = prefixsum[currsum]
                subarraysize = i - index #this
                maxlen = max(maxlen, subarraysize)

            #store prefix sum
            if currsum not in prefixsum:
                prefixsum[currsum] = i
        return maxlen

#Intuition, Think of prefix sum as your altitude
# - Equal 0s and 1s means the sum returns to the same level as before
# - If at two different times (indices), your altitude is the same, then the height gained and height lost between those points must cancel out.

##Little tricky to understand by i+1 to j --
#If prefix[i] == prefix[j]
#sum of the subarray from index i to j? prefix[j] – prefix[i-1]
# Prefix sums measure everything before the index, so the difference between equal prefix sums always corresponds to the subarray after i up to j:
# (i+1 to j).

#Idea,Interesting!!!
# - turn all 0 to -1s
# - we are trying to find longest subarray of sum zero, Now equal 0s and 1s means the subarray sum = 0.
# - Maintain a hashmap storing the first index where each prefix sum appears.
# - If the prefix sum repeats at index j (first seen at i), then the subarray (i+1 … j) has sum 0 → equal 0s and 1s.
# - Initialize prefix sum 0 at index –1 so segments starting at index 0 are counted.
#Try to visualise that sum increase when +1, decrease when -1
# If the prefix sum ever returns to a value you’ve seen before, it means everything between those two positions canceled out to zero.

        
#n2 subarrays for n elements
#cant use sliding window, cause its not possible to make a guarranted decision of when to shrink