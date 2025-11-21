class Solution:
    def mySqrt(self, x: int) -> int:
        #explore all int, Use the sorted property of integers to reduced the search space.
        #Kind of like binary search
        l,r = 0,x
        res = 0
        while l<=r:
            mid = (l+r)//2

            if  mid*mid > x:
                r = mid-1
            elif mid*mid <x:
                l = mid +1
                res = mid
            else:
                return mid
        return res
            
#bruteforce works!! - check all nums
        # if x == 0:
        #     return 0
        # if x == 1:
        #     return 1
        # res = 0
        # for num in range(x):
        #     if num * num <= x:
        #         res = num
        #     else:
        #         return res
        # return res


        