class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms) # number of rooms
        visit = set()
        def dfs(i):
            if i in visit: return # dont forget to check
            if len(visit) == n: return True
            visit.add(i)
            for key in rooms[i]:
                dfs(key)

        dfs(0)
        return len(visit) == n

#We visit each room once, and each key once.

# T - 𝑂(𝑛+total keys) = 0(n)
