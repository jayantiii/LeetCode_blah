class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixsummod = {0:1} #start
        currsum = 0
        ans = 0
        for i in range(len(nums)):
            currsum = currsum + nums[i]
            summodk = currsum % k
            if summodk in prefixsummod:
                ans += prefixsummod[summodk]

            # dont put in if block
            prefixsummod[summodk] = prefixsummod.get(summodk,0) +1
    
        return ans



#Key fact:
# If two prefix sums have the same remainder mod k, their difference (the subarray sum between them) is divisible by k.
#you compute the normal prefix sum, but what you store/count is:
# prefix_sum mod k

#----------------------------------------------------
#BRuteforce works but Tle for some
        # count = 0
        # for i in range(len(nums)):
        #     currsum = 0
        #     for j in range(i,len(nums)):
        #         currsum += nums[j]
        #         if currsum % k == 0:
        #             count+=1
        # return count

#-----------Why kadane's algo-----------------------------------
# Kadane’s algorithm cannot be used for this problem because Kadane maximizes a subarray sum, but this problem cares only about whether a subarray sum is divisible by k

# Kadane keeps just one active subarray:
# curr = max(nums[i], curr + nums[i])   # keep extending or restart
# best = max(best, curr)

# This works because of a key property for maximum sum:
# If your current sum becomes worse than just starting fresh at nums[i],
# you can safely forget the old subarray. It will never be part of an optimal answer.
# This is called an optimal substructure + greedy discard.
# The decision “drop negative prefix” is mathematically safe for maximizing sum.


        