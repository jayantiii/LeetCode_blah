class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = [1 for i in range(len(nums))]
        count = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    # Scenario 1: We found a strictly LONGER path
                    if length[i] <  length[j]+1:
                        length[i] =length[j] +1
                        count[i] = count[j] ## Reset count to j's count

                    # Scenario 2: We found another way to get the SAME max length
                    elif length[i] == length[j] +1:
                        ## Add all ways to reach j
                        count[i] += count[j] #VERY IMP!! its not   count[i] +=1

        maxlis = max(length)
        maxcount = 0
        ## Sum the counts of all indices that achieved that max_length
        for i in range(len(nums)):
            if length[i] == maxlis:
                maxcount+= count[i]
        return maxcount





#To count “number of LIS”, for each index i you must know two things about every predecessor j:
# len[j] = best LIS length ending at j
# cnt[j] = how many ways achieve that best length ending at j

# The main issue is that maxcount shouldn't just be an incrementing variable; it needs to be an array that stores how many ways you can reach a specific index with the Longest Increasing Subsequence (LIS) length ending at that index.

# Why your original logic struggledIn your code, you tried to calculate a maxcount for the current index i on the fly. The problem is that nums[i] might connect to several different previous numbers (nums[j]), each of which might already represent multiple sequences.For example, if nums[i] = 10 and it can extend two different 5s, and each 5 was reached in 3 different ways, nums[10] now has $3 + 3 = 6$ ways. You can't know that "6" without looking at count[j].

        lis = [1 for i in range(len(nums))]
        maxliscount = 0
        maxlistlength = 1
        for i in range(1,len(nums)):
            maxlis = 1
            maxcount = 1
            for j in range(i-1,-1,-1): #or can do -->  for j in range(i):
                prevmaxlis = maxlis
                if  nums[i] > nums[j]: #dont switch the vars
                    maxlis = max(maxlis, lis[j]+1)
                    if maxlis == prevmaxlis:
                        maxcount+=1
                    elif maxlis > prevmaxlis:
                        maxcount = 1
            lis[i] = maxlis
            if maxlis > maxlistlength:
                maxlistlength = maxlis
                maxlistcount = maxcount
            elif maxlis == maxlistlength:
                maxliscount = maxliscount + maxcount


        return maxliscount
        


# #how to find longesr is

# [1,3,5,4,7]

# dp = [1,2,3,4,4]

#  [1,1,1,1,1,1]

#  max number how many - length of numbe rof shse