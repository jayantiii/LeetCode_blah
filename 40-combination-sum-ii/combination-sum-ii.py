class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    #Each number in candidates may only be used once in the combination.
    # unique combinations 
        res = []
        candidates.sort() #To avoid duplicates!!

        def backtrack(i,subset,currsum):
            if i == len(candidates):
                if currsum == target:
                    res.append(subset.copy())
                return
            
             #currsum less tha target, shouldnt be more
            if currsum >target:
                return

            #Include
            backtrack(i+1, subset +[candidates[i]],currsum + candidates[i])
            #Exclude!! Imp while loop to avoid duplicates
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, subset,currsum)
    

        backtrack(0, [], 0)
        return res
        


#candidates = [2,5,2,1,2], target = 5
#create like decision tree, include or exclude
# dont go down the tree, if sum > target

#The while loop is to avoid [1,2] and again [1,2]

#Even before duplicate-skipping logic, the DFS ordering always ensures:
# numbers are chosen in increasing index order
# you never go backwards in the array
# therefore you can never build [7,1] if 1 comes before 7 in the sorted array