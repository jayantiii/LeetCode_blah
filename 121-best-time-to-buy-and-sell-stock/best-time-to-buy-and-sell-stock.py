class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        low = prices[0]
        for price in prices:
            if price < low:
                low = price
            res = max(res, price - low)
        return res
        



#brute force - doesnt pass last some cases
        # max = 0
        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j]-prices[i]  > max:
        #             max = prices[j]-prices[i]
        # return max

        