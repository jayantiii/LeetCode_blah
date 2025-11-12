class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        preq = { i:[] for i in range(numCourses)} #create adj list map
        for crs, pre in prerequisites:
            preq[crs].append(pre)

        visited = set()
        visiting = set()
        res = []
        def dfs(crs): # dont forget def
            if crs in visited:
                return True
            if crs in visiting:
                return False
            visiting.add(crs)
            for pre in preq[crs]:
                dfsres = dfs(pre)
                if not dfsres:
                    return False
                # res.append(pre) --- this is not needed!! understand recursion
            res.append(crs)
            visiting.remove(crs)
            visited.add(crs)

            return True

        for crs in range(numCourses):
            dfsres = dfs(crs)
            if not dfsres:
                return [] #empty if no possible
        return res
        