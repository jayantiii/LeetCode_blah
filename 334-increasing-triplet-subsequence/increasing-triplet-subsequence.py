class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float("inf")
        second = float("inf")
        for i in range(len(nums)):
            if nums[i] <= first: #dont forget =
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            # means nums[i] is more than f and s
            else:
                return True

        return False


#Interesting apporach, this works because we dont need to return the indices
#Inituion - keep the smallest value seen so far in first and the smallest possible "middle" value in second. If a new number exceeds second, it must be the third element of an increasing triplet because second only exists if a smaller first preceded it.

#---------------- Check if its a mid element. 0(n2)------------------------
##Pick every number in the array and see if it can be the middle element of a triplet.
        # for i in range(1,len(nums)-1):
        #     smaller, larger = False, False
        #     for j in range(i): #left side
        #         if nums[j] < nums[i]:
        #             smaller = True             
        #     for j in range(i+1,len(nums)): #right side
        #         if nums[j] >nums[i]:
        #             larger = True
        #     if smaller and larger:return True
               
        # return False
#---------------- DP recursion way. 0(n2)------------------------
#        memo = {}
        # def lis(i,previ, length): #l is length of IS
        #     if length == 3:
        #         return True
        #     if i == len(nums): return False

        #     if (i,previ,length) in memo:
        #         return memo[(i,previ,length)]

        #     #skip
        #     skip = lis(i+1,previ, length)

        #     #Pick ( if its first index or larger)
        #     take = False
        #     if previ == -1 or nums[i] > nums[previ]:
        #         take = lis(i+1,i,length+1)
            
        #     res = skip or take
        #     memo[(i,previ,length)] = res
        #     return res

        # return lis(0,-1,0) #start state

#------------------- #Two - sum type apporach - 0(n2) ------------------
#Two - sum type apporach, In Increasing Triplet, we can't look for a single number, but we can store "valid pairs" we've already found.

    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     # seen_as_second stores numbers that have at least 
    #     # one smaller number to their left.
    #     seen_as_second = set()
        
    #     for i in range(n):
    #         # "Two Sum" logic: Check if any value in our set 
    #         # can act as the 'middle' for the current 'nums[i]'
    #         for val in seen_as_second:
    #             if nums[i] > val:
    #                 return True
            
    #         # Now update the set: check if current nums[i] 
    #         # can be a 'middle' for any previous nums[j]
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 seen_as_second.add(nums[i])
    #                 break # We only need to know it's a valid middle once
                    
    #     return False

#------------------------  0(n3) --------------
# My Bruteforce - 0(n3)
# for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 for k in range(j,len(nums)):
#                     if nums[i] < nums[j] <nums[k]:
#                         return True
#         return False

#---------------------------
# Note - To determine if an $O(n^2)$ solution will pass, you can use a simple "Rule of Thumb" based on the total number of operations.The $10^8$ RuleMost Online Judges (LeetCode, Codeforces, etc.) can handle roughly $10^7$ to $10^8$ operations

