from math import isqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                s = a*a + b*b
                c = isqrt(s)              # exact integer floor sqrt
                if c <= n and c*c == s:   # perfect square check
                    res += 1
        return res
        