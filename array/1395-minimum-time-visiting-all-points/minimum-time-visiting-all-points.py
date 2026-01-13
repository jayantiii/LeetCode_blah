class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    # distance bw 2 points is max diff of one coord ( x or y) - Interesting!!
        x1,y1 = points.pop()
        res = 0
        while points: # since we popping
            x2, y2 = points.pop()
            res += max(abs(y2-y1), abs(x2-x1))
            x1,y1 = x2,y2 # dont forget this

        return res

        