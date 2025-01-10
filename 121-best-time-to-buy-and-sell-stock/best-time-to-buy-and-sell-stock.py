class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]
        for price in prices:
            if price < low:
                low = price
            res = max(res, price - low)
        return res

#can use 2 pointer, try!

# dp!?
# min_price = float('inf')
#         max_profit = 0
#         for current_price in prices:
#             min_price = min(current_price, min_price)
#             max_profit = max(max_profit, current_price - min_price)   
#         return max_profit

        

#brute force - doesnt pass last some cases
        # max = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]  > max:
        #             max = prices[j]-prices[i]
        # return max

        