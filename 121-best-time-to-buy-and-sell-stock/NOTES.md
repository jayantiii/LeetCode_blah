https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/1144842/Several-solutions-in-Python          -- look in this link for more
​
**#this failed cause more time complexicity**
def maxProfit(self, prices: List[int]) -> int:
N = len(prices)
maxprofit = 0
for i in range(N):
for j in range(i+1,N):
if prices[i] < prices[j]:
maxprofit=max(maxprofit,prices[j]-prices[i])
return maxprofit
​
​