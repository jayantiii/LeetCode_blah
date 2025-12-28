class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set() #needed so that u dont bounce back and forth
        def recursion(i):
            if i >=len(arr) or i < 0: return False
            if arr[i] == 0:
                return True
            if i in visited:
                return False
            visited.add(i)
            return recursion(i+arr[i]) or recursion(i-arr[i])
            
        return recursion(start)




        