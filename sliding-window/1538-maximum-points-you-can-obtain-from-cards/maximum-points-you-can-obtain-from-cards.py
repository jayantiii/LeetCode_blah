class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        maxsum = sum(cardPoints[:k])  
        l,r = k,n
        currsum = maxsum        
        while r > n-k: ## or  -- while l > 0
            l-=1
            r-=1
            ldel = cardPoints[l]
            radd = cardPoints[r]

            currsum = currsum -  ldel +  radd  #update currsum
            maxsum = max(maxsum, currsum)

        return maxsum
   
# translating this problem into minimum sub-array

#------Backtracking, TLE-----------------------------------------------
#IMP!!
#Instead of passing whole points array -->
##we can just use pointers l and r to keep track!!

        # points = cardPoints
        # def backtrack(cards,points):
        #     if not points:
        #         return 0
        #     if cards == k:
        #         return 0

        #     #pickleft
        #     left = points[0] + backtrack(cards+1,points[1:])

        #     #pickright
        #     right = points[-1] + backtrack(cards+1, points[:-1])

        #     return max(left,right)

        # return backtrack(0,points)

#------------------DP IDEA----------------------------------
# dp[i] = sum of first i cards (take i from left)
# suffix[j] = sum of last j cards (take j from right)
# Answer = max(dp[i] + suffix[k-i]) for i=0..k.

