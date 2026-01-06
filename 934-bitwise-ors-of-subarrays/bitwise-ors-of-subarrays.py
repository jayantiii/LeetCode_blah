class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        #O(32n)
#idea: keep only the distinct OR values of subarrays that end at the current index.
        unique = set()
        prevind = set()
        for i in range(len(arr)):
            newset = {arr[i]}
            unique.add(arr[i]) 
            for orval in prevind: #this can be max 32
                newor = orval | arr[i]
                newset.add(newor)   #dont forget  
                unique.add(newor)          
            prevind = newset
        return len(unique)

     
#prevind = set of ORs for subarrays ending at previous index
#don’t enumerate subarrays. Track only the distinct OR results of subarrays ending at each index.

#Can write ---> unique |= newset means union-update.
# It updates unique by adding all elements from newset into it (in place).

#Because OR results along “keep extending the subarray” form a chain that can only turn bits on, and there are only ~32 bits to turn on.

# # -------------------brute force -------------------- 
#         unique = set()
#         for i in range(len(arr)): #start point
#             bitor = 0
#             for i in range(i,len(arr)): #endpoint
#                 bitor = bitor | arr[i] #OR symbol
#                 unique.add(bitor)

#         return len(unique)