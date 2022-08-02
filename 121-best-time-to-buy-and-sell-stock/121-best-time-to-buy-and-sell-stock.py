class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        maxprofit = 0
        minpurchase = prices[0]
        for i in range(1,N):
            curprofit = prices[i] - minpurchase
            if maxprofit < curprofit :
                maxprofit = curprofit
            if prices[i] < minpurchase:
                minpurchase = prices[i]
                
        return maxprofit

# The thing is that using min/max functions takes much more time than if/else statemtns.
  
# def maxProfit(self, prices: List[int]) -> int:
# 	if not prices:
# 		return 0

# 	maxProfit = 0
# 	minPurchase = prices[0]
# 	for i in range(1, len(prices)):		
# 		maxProfit = max(maxProfit, prices[i] - minPurchase)
# 		minPurchase = min(minPurchase, prices[i])
# 	return maxProfit

                
                
        
        