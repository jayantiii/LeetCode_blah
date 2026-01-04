class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        def maxwater(emptybottles):
            if emptybottles < numExchange:
                return 0
            fullbottle = emptybottles//numExchange
            remain = emptybottles % numExchange
            final =  fullbottle + maxwater(fullbottle + remain )
            return final

        return numBottles + maxwater(numBottles)



        