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


# Above and below both soln same time and space O(n), O(n)

#Greedy dont work here!
# Greedy works in some jump games because movement is one-directional (only forward) and the “best reach so far” is monotone. Jump Game III is different: you can go left or right, so you get cycles and branching → that’s a graph reachability problem. Interview tell: “two-way moves + possible revisits ⇒ need visited ⇒ BFS/DFS.”
#----------------Iterative BFS/DFS (safer than recursion depth)-----------------
# class Solution:
#     def canReach(self, arr: List[int], start: int) -> bool:
#         n = len(arr)
#         q = deque([start])
#         seen = {start}

#         while q:
#             i = q.popleft()
#             if arr[i] == 0:
#                 return True

#             for ni in (i + arr[i], i - arr[i]):
#                 if 0 <= ni < n and ni not in seen:
#                     seen.add(ni)
#                     q.append(ni)

#         return False




        