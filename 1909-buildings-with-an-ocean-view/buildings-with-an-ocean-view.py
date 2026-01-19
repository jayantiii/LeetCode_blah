class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        highest = -1
        for i in range(len(heights)-1,-1,-1):
            if heights[i] >  highest:
                res.append(i)
                highest = heights[i]

        return res [::-1]

        