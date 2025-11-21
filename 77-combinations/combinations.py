class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #height of decision tree will be k
        #  time - n power k
        res = []
        def backtrack(i,subset):
            if len(subset) == k: # k elements, dont do i == k!
                res.append(subset.copy())
                return

            for j in range(i,n+1): # start from i cause no repeat
                # subset.append(j)
                backtrack(j+1, subset + [j])
                # subset.pop() # remove so that we continue in loop

        backtrack(1,[])
        return res






#[1,2,3,4] can either choose 1, 2,3 or 4 then go ahead and make tree

        