class HitCounter:

    def __init__(self):
        self.arr = []

    def hit(self, timestamp: int) -> None:
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        diff = timestamp - 300
        left = bisect.bisect(self.arr, diff)
        
        return len(self.arr[left:])
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

#Use binary search, as timestamps are in sorted order
#But it’s only good if you never evict and you’re okay with memory growing over time.

#------- Follow up: What if the number of hits per second could be huge? Does your design scale?

#---- queue soln ------------
# from collections import deque

# class HitCounter:
#     def __init__(self):
#         self.q = deque()      # (timestamp, count)
#         self.total = 0

#     def _evict(self, t: int):
#         cutoff = t - 300
#         while self.q and self.q[0][0] <= cutoff:
#             _, cnt = self.q.popleft()
#             self.total -= cnt

#     def hit(self, timestamp: int) -> None:
#         self._evict(timestamp)
#         if self.q and self.q[-1][0] == timestamp:
#             ts, cnt = self.q.pop()
#             self.q.append((ts, cnt + 1))
#         else:
#             self.q.append((timestamp, 1))
#         self.total += 1

#     def getHits(self, timestamp: int) -> int:
#         self._evict(timestamp)
#         return self.total

# we use queue and not hashmap cause Using a hashmap alone isn’t wrong for correctness. The problem is efficiency: a hashmap has no ordering, so you can’t cheaply remove “oldest timestamps” or count hits in the last 300 seconds without extra work.
