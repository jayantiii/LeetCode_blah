from math import ceil
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = {i:[] for i in range(len(roads)+1)}

        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)

        sys.setrecursionlimit(300000)

        #Return the number of people in the subtree rooted at node.
        visited = set()
        def minfuel(node):
            visited.add(node)

            people = 1
            fuel = 0
            for nei in graph[node]:
                if nei not in visited:
                    childpeople, childfuel = minfuel(nei)
                    people +=  childpeople
                    fuel += childfuel

            if node !=0:
                 fuel += ceil(people / seats)
            return people, fuel #return both
 
        people, fuel = minfuel(0)
        return fuel


#If x people meet on the same node, what is the minimum number of cars needed?#
# ---fuel =  x // seats (roundup) #try to figure fast
#Hint: The fact that there is exactly n - 1 roads means that there's only one path to a given node from 0#

###---------------------------Mistakes while coding----------------------
#use visited set or pass param parent to make sure u dont loop forever

#You can return only fuel, but not by passing people as a parameter in a single DFS: subtree-people is computed bottom-up, so it’s an output of children, not an input you already have while going down.#

#fuel = (people + seats - 1) // seats #round up formula   # ceil(people / seats)

#no .left or .right pointers there, use neighbours

#You do count the capital’s representative in subtree sizes, because they exist. You just don’t add fuel for node 0, since it has no parent edge to travel up.

# if node in visited and node.val == 0: # return people, fuel
#This is not needed in start

#Yes in general building the graph terms it’s O(n + m).
#Here it’s a tree, so m = n - 1, which collapses to O(n).

##-------------- Cleaned up, simpler ---------------------------------
#just return the people using recursion, no need to calc fuel in recursion-------
#   res = 0
#         def dfs(node: int, parent: int) -> int:
#             nonlocal res
#             passengers = 0
#             for child in adj[node]:
#                 if child == parent:
#                     continue
#                 p = dfs(child, node)          # people in child's subtree
#                 passengers += p
#                 res += ceil(p / seats)        # fuel for edge child -> node
#             return passengers + 1             # include this node's person

#         dfs(0, -1)
#         return res


