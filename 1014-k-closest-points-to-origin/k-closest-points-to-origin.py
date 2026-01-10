class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = [] #(dist, index)
        res = []
        for i, p in enumerate(points):
            x,y = p[0],p[1]
            dist = x**2  + y**2
            heapq.heappush(minheap,(dist,i))

        while k > 0:
            dist, i = heapq.heappop(minheap)
            res.append(points[i])
            k-=1

        return res

        