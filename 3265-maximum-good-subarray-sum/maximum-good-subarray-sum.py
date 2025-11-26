class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixsum = {} #store sum till that number excluding it
        currsum = 0
        maxsum = float('-inf')
        for j in range(len(nums)):
            #look if a starting point present for it
            # 1) check both possibilities: x+k and x-k
            if  nums[j] - k in prefixsum:
                remain =  nums[j] - k
                subarraysum = currsum + nums[j] - prefixsum[remain]
                maxsum = max(maxsum, subarraysum) #should be inside if
            if nums[j] + k in prefixsum:
                remain =  nums[j] + k
                subarraysum = currsum + nums[j] - prefixsum[remain]
                maxsum = max(maxsum, subarraysum)
        
           #  2) update prefixsum for this value using prefix BEFORE x
            if nums[j] in prefixsum:
                prefixsum[nums[j]] = min(prefixsum[nums[j]],currsum)
            else:
                prefixsum[nums[j]] = currsum
            #3) add the currvalue
            currsum+=nums[j]
           
        return 0 if maxsum == float('-inf') else maxsum



#how to chose which prefixsum to store when 2 same number
# subarraysum = prefix(later) - prefix(earlier)
#Notice that for subarraysum to be more we need to minimise the prefix(earlier)!!!
# Prefix sum solution, think more to understand

# A good subarray nums[i..j] must satisfy:
#       |nums[i] - nums[j]| = k

#   1) nums[i] - nums[j] = k
#      → nums[i] = nums[j] + k
#
#   2) nums[j] - nums[i] = k
#      → nums[i] = nums[j] - k
# So we only need to check:
#         if (x + k) was seen earlier
#         if (x - k) was seen earlier

#Bruetforce works, interesting!!
        # maxsum = float("-inf")
        # for i in range(len(nums)):
        #     currsum = 0
        #     for j in range(i, len(nums)):
        #         currsum += nums[j]
        #         if abs(nums[j] - nums[i]) == k: #abs value
        #             maxsum = max(currsum, maxsum)
        # return 0 if maxsum == float("-inf") else maxsum #this needed
                
        