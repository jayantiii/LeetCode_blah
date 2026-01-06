class Solution:
    def numSquares(self, n: int) -> int:
        INF = float("inf")

        @lru_cache(None)
        def perfectsqaures(n):
            if n == 0: #reached length
                return 0 #return zerooo, not 1

            if n < 0: #invalid path
                return INF

            res = float("inf") #start at max
            for i in range(1,n+1): # or better range(1,isqrt(n) + 1)
                square = i*i
                newnumber = n - square
                if newnumber >=  0:
                    res = min(res, 1 + perfectsqaures(newnumber)) #MAIN!
                else:
                    break

            return res
        return perfectsqaures(n)


# For those who are interested in Algorithmic Number Theory, there is a very interesting theorem that can solve the problem directly without recursion.

# It is called Lagrange’s Four-Square Theorem, which states: every natural number can be represented as the sum of four integer squares.

# It was proven by Lagrange in 1770.

# Applying to our problem NumSquares(n) can only be 1, 2, 3, or 4. Not more.

# It turns into the problem of identifying when NumSquares(n) returns 1, 2, 3, or 4.
        