import numpy as np
class Solution:
    def isHappy(self, n: int) -> bool:
        #had to think much to understand when and how to stop cycle.
        # idea is to have a seen array
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
            if res in seen:
                return False
            seen.append(res)

# i tried using this below logic to stop cycle, this is wrong because -->
# ---> if example = 7 then 7*7 = 49 and it should continue and not stop at 7

# if res < 10:    
#     print("here")
#     return False
            



            

        