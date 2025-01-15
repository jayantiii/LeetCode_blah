import numpy as np
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        while True:
            res = 0
            if n < 10 and not 1:
                return False
            for digit in str(n):
                res += int(digit)**2
            print(res)
            n = res
            if res ==1: return True
            # if res < 10:
            #     print("here")
            #     return False
            if res in seen:
                return False
            seen.append(res)

            



            

        