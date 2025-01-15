import numpy as np
class Solution:
    def isHappy(self, n: int) -> bool:
        #had to think much to understand when and how to stop cycle.
        # idea is to have a seen array
        seen = []
        while True:
            res = 0
            for digit in str(n):
                res += int(digit)**2
            print(res)
            n = res
            if res ==1: return True
            if res in seen:
                return False
            seen.append(res)

# i tried using this below logic to stop cycle, this is wrong because -->
# ---> if example = 7 then 7*7 = 49 and it should continue and not stop at 7

# if res < 10:    
#     print("here")
#     return False
            
##neetcode ans -- more efficient whats complexity)
#  visit = set()  # MEMO to track visited numbers

#     while n not in visit:
#         visit.add(n)
#         n = self.sumOfSquares(n)

#         if n == 1:
#             return True

#     return False

# def sumOfSquares(self, n: int) -> int:
#     output = 0

#     while n:
#         digit = n % 10
#         digit = digit ** 2
#         output += digit
#         n = n // 10

#     return output



            

        