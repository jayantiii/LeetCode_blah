class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= max(candies):
                result[i] = True
        return result
        






# ask questions like can multiple kids can have the greatest number of candies.