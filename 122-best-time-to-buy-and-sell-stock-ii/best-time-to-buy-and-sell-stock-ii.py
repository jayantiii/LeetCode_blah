class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]: #price increase, means buy and sell
                maxprofit+= prices[i] -  prices[i-1]
        return maxprofit

    

#So what we do is buy when di


# At first I thought this problem was more complicated. Surely you can't just always sell the next day if it goes higher, right? But yes that really is the solution. What if it goes up a little then down a little then up a lot though, might it be better to hold all the way from the first to the last? No, because we can freely sell and buy on any day with no fee, so we sell before it goes down a bit, then buy again once its down, then sell again once it goes even higher. But then what if it continues to increase, shouldn't you hold then? Again, no because we can just buy again right after we sell, so there's no difference between holding through 2 increasing days and selling and buying in-between

