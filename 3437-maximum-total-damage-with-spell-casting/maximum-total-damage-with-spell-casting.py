class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        #dp[i] -> max damage given 0.1....i spells
        #dp over unique values and keep a counter!!

        count = Counter(power)
        uniquevals = sorted(count)
        m = len( uniquevals)

        dp = [0]*m #  dp[i] = best using vals[0..i]
        dp[0] =  uniquevals [0]*count[ uniquevals [0]]

        for i in range(1,m):
            #skip
            skip = dp[i-1]

            #take
            earn =  uniquevals [i]*count[uniquevals[i]]
            j = i-1

            #  find previous index j that DOES NOT conflict:
            # conflict range is [x-2, x-1] (and also x+1, x+2 but those are future)

            while j >= 0 and uniquevals[j] >=  uniquevals[i] -2: #IMP!!
                j-=1
            take = earn + dp[j]

            dp[i] = max(skip,take)

        return dp[-1]
                
#Read question carefully!
#it's power[i] + 1 etc., not power[i + 1]. Just saved ya some 10 minutes of debugging.

#---------------------Recursion and bineary search-----------------------------
        # power.sort() #nlogn

        # @lru_cache(None)
        # def dfs(i): #
        #     if i < 0 or i >= n:
        #         return 0

        #     #skip
        #     skip = dfs(i+1)

        #     # take: take all copies of value v
        #     takevalue = 0
        #     value = power[i]
        #     j = i
        #     while j < n and power[j] == value:
        #         takevalue += power[j]
        #         j+=1

        #     # next allowed index: first value > v + 2 -> since its sorted

        #IMP -->  or use --> k = bisect_right(power, v + 2, j, n)

        #     while j < n and value < power[j] <= value + 2:
        #         j+=1

        #     take = takevalue  + dfs(j)
        #     return max(skip,take)

        # return dfs(0)

        # dfs(0)
