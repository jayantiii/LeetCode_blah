from math import ceil
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = {i:[] for i in range(len(roads)+1)}

        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)

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

##--- Code using subtree array-----------------------------------------
#         """
#         Idea:
#         - Tree is rooted at node 0 (capital).
#         - Each node has exactly 1 representative (1 person).
#         - Everyone must move upward toward 0 along the unique path in the tree.
#         - If a subtree has P people total, then across the edge from that subtree root to its parent,
#           we must transport P people. With `seats` per car, fuel on that edge is ceil(P / seats).
#         - Therefore:
#               total fuel = sum_{v != 0} ceil(subtree_people[v] / seats)
#           where subtree_people[v] is the number of people in v's subtree (including v).

#         Steps:
#         1) Compute subtree_people[] using DFS.
#         2) Compute fuel by summing ceil(subtree_people[v] / seats) for all non-root nodes.
#         """

#         # Python recursion depth default is ~1000, but a tree can be a long chain of length up to ~1e5,
#         # so DFS recursion would crash without increasing the limit.
#         sys.setrecursionlimit(300000)

#         # Build adjacency list for the undirected tree
#         n = len(roads) + 1
#         adj = [[] for _ in range(n)]
#         for u, v in roads:
#             adj[u].append(v)
#             adj[v].append(u)

#         # subtree[v] = number of people in subtree rooted at v (including v itself)
#         subtree = [0] * n

#         def dfs(node: int, parent: int) -> int:
#             """
#             Returns: number of people in node's subtree.

#             Since each node contributes 1 person, start with people = 1.
#             Add all child-subtree counts (excluding the parent to avoid going back up).
#             Store the result into subtree[node] so we can compute fuel later.
#             """
#             people = 1  # this node's representative
#             for child in adj[node]:
#                 if child == parent:
#                     continue
#                 people += dfs(child, node)

#             subtree[node] = people
#             return people

#         # Root the tree at 0 and fill subtree[]
#         dfs(0, -1)

#         # Now compute fuel independently from subtree sizes:
#         # For each non-root node v, edge (v -> parent[v]) must carry subtree[v] people.
#         fuel = 0
#         for v in range(1, n):  # skip root (no edge above it)
#             fuel += ceil(subtree[v] / seats)

#         return fuel


# # Example run (mental):
# # roads = [[0,1],[0,2],[1,3],[1,4]], seats=2
# # subtree[3]=1, subtree[4]=1
# # subtree[1]=1+1+1=3
# # subtree[2]=1
# # fuel = ceil(3/2)+ceil(1/2)+ceil(1/2)+ceil(1/2) = 2+1+1+1 = 5


