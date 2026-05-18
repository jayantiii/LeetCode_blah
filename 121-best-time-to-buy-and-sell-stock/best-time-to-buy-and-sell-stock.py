class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        minpurch = prices[0]
        for i in range(1,len(prices)):
            currp = prices[i] - minpurch
            maxp = max(maxp,currp)
            minpurch = min(minpurch, prices[i])

        return maxp

        
