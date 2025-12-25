"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #lets do bfs
        emp_by_id = {e.id: e for e in employees} #Imp step
        importance = 0
        q = deque([id])
        while q:
            empid = q.popleft()
            importance +=  emp_by_id[empid].importance
            subordinates =  emp_by_id[empid].subordinates

            for sub in subordinates:
                q.append(sub)

        return importance 


# -------------My mistake -----------------------------
#1) I wrote like this below
    #    emp = q.popleft()
    #         importance += emp.importance
# -- You’re queueing IDs, but then treating the popped value like an Employee object (emp.importance). Fix: build an id -> Employee lookup first, then BFS/DFS over IDs.

#2) I forgot visit set, but here i dont need but safe to have

            
        