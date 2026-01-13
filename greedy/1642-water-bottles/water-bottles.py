class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
#ItsRecursive soln, Main hint --> we have to keep reapeating the exchange process!  
# Time:  O(log_e n)  where n = numBottles, e = numExchange
# Space: O(log_e n)  recursion stack 
        def maxwater(emptybottles):
            if emptybottles < numExchange:
                return 0
            fullbottle = emptybottles//numExchange
            remain = emptybottles % numExchange
            final =  fullbottle + maxwater(fullbottle + remain )
            return final

        return numBottles + maxwater(numBottles)

# Why log base e?
# Each step exchanges empties for full: full = empty // e.
# So the number of full bottles you get shrinks by about a factor of e each recursion/iteration
# (like repeatedly dividing by e), which takes ~log_e(n) steps until it becomes 0.

#iterative soln
#         total = 0
#         empty = 0
#         full = numBottles

#         while full > 0:
#             total += full
#             empty += full
#             full = empty // numExchange
#             empty %= numExchange

#         return total



        