class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = {} #stores indices
        cols = {}
        visited = set() #store indices
        for i in range(len(stones)):
            x,y = stones[i]
            if x not in rows:
                rows[x] = []
            if y not in cols:
                cols[y] = []

            rows[x].append(i) #append indice
            cols[y].append(i) 

        #DFS should take a stone index (not (x,y)), because you need to mark stones visited.         
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for x in rows[stones[i][0]]:
                dfs(x)
            for y in cols[stones[i][1]]:
                dfs(y)
                  
        components = 0
        for i in range(len(stones)):
            if i in visited:
                continue
            dfs(i)
            components +=1

        return len(stones) - components



# to figure out the intuition - that componenet will form with same row and col stones and then we can always remove all sones left 1 at last but how to make componenets in implementation is tricky
#Don’t build a 2D matrix to do dfs. The coordinates can be huge/sparse, so a grid is wasted work.

# DFS clue: think connected components.
# Make a graph where stones are nodes.
# Edge between stone i and j if they share row or column.
# In any connected component of size k, u can remove k-1, leaving 1

# HINT 1 :
# Instead of viewing this question as "Remove the maximum number of stones with the same rows and columns", you may take this question to be "What is the number of stones that can be reached from one another, if reaching stone A to stone B requires either stone A and B having same row or column.

# HINT 2 :
# Let us assume that the number of given stones is "num"
# If we look at all the stone clusters connected to one another, what is the number of stones that you can remove?
# Example : In the below given grid, if '0' represents stones
# X X 0 X X
# 0 X 0 X X
# X X X X X
# 0 X X X 0

# We can map all the stones to one another using basic traversal algorithms.
# For EACH SUCH CLUSTER of stones that can be connected in the grid, the number of stones that can be removed is number of stones in that cluster - 1.

# If we now add the number of clusters and all the number of stones that can be remove :-
# (Stones in Cluster 1- 1) + (C2 -1) + (C3 -1) + ......
# = C1 + C2 + C3 +..... - (number of clusters)
# = Total number of stones - Number of Clusters

# Which will be the solution to this problem.