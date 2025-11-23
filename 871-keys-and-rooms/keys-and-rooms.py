class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms) # number of rooms
        visit = set()
        def dfs(i):
            if i in visit: return
            if len(visit) == n: return True
            visit.add(i)
            for key in rooms[i]:
                dfs(key)

        dfs(0)
        return len(visit) == n

       
        

#rooms = [[1,3],[3,0,1],[2],[0]]