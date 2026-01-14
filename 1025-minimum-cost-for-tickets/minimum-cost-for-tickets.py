class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def mincost(i):
            if i == len(days):
                return 0

            oneday = costs[0] + mincost(i+1)

            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j+=1

            sevenday = costs[1] + mincost(j)

            while j < len(days) and days[j] < days[i] + 30:
                j+=1

            thirtyday = costs[2] + mincost(j)

            return min(oneday,sevenday,thirtyday)


        return mincost(0)

        