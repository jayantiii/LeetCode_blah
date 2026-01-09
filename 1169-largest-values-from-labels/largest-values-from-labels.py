class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        #its greedy, sort but zip value and labels
        sortvalues = sorted(zip(values,labels), key = lambda x:x[0], reverse = True)
        labelcount = {}
        totalsum = 0
        picked = 0
        for value, label in sortvalues:
            if labelcount.get(label,0) == useLimit:
                continue
                
            totalsum = totalsum + value
            picked+=1
            labelcount[label] = labelcount.get(label,0) +1
            
            if picked == numWanted:
                return totalsum
            
        return totalsum #return totalsum, not 0
            
            
##---- Backtracking clean----------------------------------------
# In backtracking below, see how to undo the hasmap , dont do -=1 and all

# def backtrack(i: int, count: int, used: Dict[int, int]) -> int:
#             if i == n or count == numWanted:
#                 return 0

#             # skip
#             best = backtrack(i + 1, count, used)

#             # take (if allowed)
#             lab = labels[i]
#             prev = used.get(lab, 0)
#             if prev < useLimit:
#                 used[lab] = prev + 1
#                 best = max(best, values[i] + backtrack(i + 1, count + 1, used))
#                 used[lab] = prev  # IMPP--restore (no del needed)

#             return best

#         return backtrack(0, 0, {})


# #------cant lru cache hasmap-------------------------------------------
# When the cache tries to store the result for (i, count, used), it crashes because used is a dict.


##---- My backtracking - lil leaky------------------------------------------------
#Whats wrong

# Your dict state isn’t restored cleanly: 
# you add/keep keys (like label: 0) and never fully undo mutations,
# so one branch can affect what another branch “sees” (state leakage).
# It may still return the right answer by luck because 0 often behaves like “not present,” but it’s fragile and will break immediately Proper backtracking must leave the dict exactly as it was before the recursive call.

#         n = len(values)
#         maplabel = {} # {labels:timesofuse}
        
#         def backtrack(i,count,hashmap):
#             if i == n:
#                 return 0  #maxsum/?
            
#             if count == numWanted:
#                 return 0
            
#             #skip
#             skip = backtrack(i+1,count,hashmap)
            
#             #take
#             #check that use limit is not over for that label
#             take = 0
#             label = labels[i]
            
#             if label not in hashmap:
#                     hashmap[label] = 0
                    
#             if hashmap[label] < useLimit:
#                 hashmap[label] +=1
#                 take = values[i] + backtrack(i+1,count+1,hashmap)
                
#                 hashmap[label] -=1
            
#             return max(skip,take)
            
            
#         return backtrack(0,0, maplabel)
        



        