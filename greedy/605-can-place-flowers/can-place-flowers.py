class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
 #O(n)
        for i,x in enumerate(flowerbed):
            if i== len(flowerbed) -1 and x ==0  and flowerbed[i-1]==0: 
                n = n-1
                flowerbed[i] = 1
            elif i == 0 and x ==0 and flowerbed[i+1]==0:
                n = n-1
                flowerbed[i] = 1

            elif x == 0 and flowerbed[i-1] ==0 and flowerbed[i+1] ==0:
                # dont by mistakely write x[i-1], its not subscriptable
                n = n-1
                flowerbed[i] = 1 # dont forget this step, occupying it
            
        return n <=0   # this how u return for true or false

#cleaner version of above code
# for i, x in enumerate(flowerbed):
#             if x == 0:
#                 prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
#                 next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

#                 if prev_empty and next_empty:
#                     flowerbed[i] = 1
#                     n -= 1
#                     if n == 0:
#                         return True
#         return n <= 0


# another wayy
# #def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         i = 0
#         while i < len(flowerbed):
#             if flowerbed[i] == 1:
#                 i += 2  # skip next one; cannot plant there
#             else:
#                 left = i == 0 or flowerbed[i - 1] == 0
#                 right = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
#                 if left and right:
#                     flowerbed[i] = 1
#                     n -= 1
#                     if n == 0:
#                         return True
#                     i += 2  # skip next one (just planted)
#                 else:
#                     i += 1
#         return n <= 0