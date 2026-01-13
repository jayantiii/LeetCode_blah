class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1) #distinct ways for 0,1...n
        memo[0] = 1
        memo[1] = 1

        for i in range(2,n+1): #run till n+1
            memo[i] = memo[i-1] + memo[i-2]
            print(memo)

        return memo[n]
        