class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        m = len(baskets)
        output = n
        for i in range(n):
            for j in range(m):
                if fruits[i] <= baskets[j]:
                    baskets[j] = float("-inf")
                    output -=1
                    break #imp to break
        return output



        

#fruits, basket , n
#how to say this basket has been taken, (float(-inf))
