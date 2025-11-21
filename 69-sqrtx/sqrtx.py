class Solution:
    def mySqrt(self, x: int) -> int:
        #explore all int, Use the sorted property of integers to reduced the search space.
        if x == 0:
            return 0
        if x == 1:
            return 1
        res = 0
        for num in range(x):
            if num * num <= x:
                res = num
            else:
                return res
        return res


        