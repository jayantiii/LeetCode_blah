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


        