class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create a adjacency preq list map
        preq = { i:[] for i in range(numCourses)}
        print(preq)

        for crs, pre in prerequisites:
            preq[crs].append(pre)
        
        # dont just do (), then thats tuple
        visitingset = set() # keep track of current dfs path
        visitedset = set() # nodes completely processed 
        def dfs(crs):
            #Base cases
            if crs in visitingset:
                return False
            if crs in visitedset: 
                return True
            
            visitingset.add(crs)
            # loop through neighbours of crs
            for pre in preq[crs]:
                dfsres = dfs(pre)
                if not dfsres:
                    return False
            visitingset.remove(crs)
            visitedset.add(crs)
            return True

        # we do this in case graph has disconnected components
        for crs in range(numCourses):
            dfsres = dfs(crs)
            if not dfsres:
                return False
        return True
              

##Note- Dont do if else return true/false statements. return true is outside of for loop, so that u just dont return it without completion and on first loop only
             

# Wrong!!!! I was doing this but it was returning on first neighbour(pre) we inspect itself 
#also, You add to visitset but return before removing it in several paths, leaving the node “stuck” as visiting and creating false cycle detections.   
#       preq[pre] = [] , this is not needed!!

#  for pre in preq[crs]:
#                 dfsres = dfs(pre)
#                 if dfsres:
#                     preq[pre] = []
#                     return True
#                 else:
#                     return False


#Hint

#This problem can be lil equivalent to finding if a cycle exists in a directed graph. 
#If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
        