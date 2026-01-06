class Solution:
    def numSquares(self, n: int) -> int:
        # O(n·sqrt(n)) time, O(n) memory. 
        # dp[x] = minimum number of perfect squares that sum to x.

        dp = [n for i in range(n+1)] #max will be n--> 1 + 1 +..
        dp[0] , dp[1] = 0, 1

        for i in range(1,n+1):
            for j in range(1,floor(math.sqrt(i))+1):
                #j*j -  # for dp[i] you only try perfect squares that are ≤ i.
                dp[i] = min(dp[i], dp[i- (j*j)] + 1) #I was so confused here!!!
               
        return dp[n]

      
#Maths Way---------------------------------
# For those who are interested in Algorithmic Number Theory, there is a very interesting theorem that can solve the problem directly without recursion.

# It is called Lagrange’s Four-Square Theorem, which states: every natural number can be represented as the sum of four integer squares.

# It was proven by Lagrange in 1770.

# Applying to our problem NumSquares(n) can only be 1, 2, 3, or 4. Not more.

# It turns into the problem of identifying when NumSquares(n) returns 1, 2, 3, or 4.

#DP example to understand---------------------------------------
# We compute dp[1]..dp[9]:
# dp[1]: try 1 → dp[0]+1 = 1 → dp[1]=1
# dp[2]: try 1 → dp[1]+1 = 2 → dp[2]=2
# dp[3]: try 1 → dp[2]+1 = 3 → dp[3]=3
# dp[4]: try 1 → dp[3]+1 = 4, try 4 → dp[0]+1 = 1 ✅ → dp[4]=1
# dp[5]: try 1 → dp[4]+1 = 2, try 4 → dp[1]+1 = 2 → dp[5]=2
# dp[6]: try 1 → dp[5]+1 = 3, try 4 → dp[2]+1 = 3 → dp[6]=3
# dp[7]: try 1 → dp[6]+1 = 4, try 4 → dp[3]+1 = 4 → dp[7]=4
# dp[8]: try 1 → dp[7]+1 = 5, try 4 → dp[4]+1 = 2 ✅ → dp[8]=2 (4+4)
# dp[9]: try 1 → dp[8]+1 = 3, try 4 → dp[5]+1 = 3, try 9 → dp[0]+1 = 1 ✅ → dp[9]=1 (9)

# Final array up to 9:
# dp = [0,1,2,3,1,2,3,4,2,1]
# #--------------------------------Recursion----------------------------------
# Without memo: Each state branches up to sqrt(n) choices, depth up to n 
# => O((sqrt(n))^n)
# With memo: each rem = n solved once, and each solve tries up to sqrt(rem) squares →   
#=> n · sqrt(n) time, n memory.

# # So time is O(n√n).
#   INF = float("inf")

#         @lru_cache(None)
#         def perfectsqaures(n):
#             if n == 0: #reached length
#                 return 0 #return zerooo, not 1

#             if n < 0: #invalid path
#                 return INF

#             res = float("inf") #start at max
#             for i in range(1,n+1): # or better range(1,isqrt(n) + 1)
#                 square = i*i
#                 newnumber = n - square
#                 if newnumber >=  0:
#                     res = min(res, 1 + perfectsqaures(newnumber)) #MAIN!
#                 else:
#                     break

#             return res
#         return perfectsqaures(n)

        