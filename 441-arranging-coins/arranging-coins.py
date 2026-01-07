class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 0
        while n >= 0: 
            row+=1 # this first then next line
            n = n-row 

        #row is the last incompelete
        return row -1


# Binary Search Approach
# class Solution:
#     def arrangeCoins(self, n: int) -> int:
#         left,right=1,n
#         while left<=right:
#             mid=(right+left)//2
#             num=(mid/2)*(mid+1)
#             if num<=n:
#                 left=mid+1
#             else:
#                 right=mid-1
#         return right

        