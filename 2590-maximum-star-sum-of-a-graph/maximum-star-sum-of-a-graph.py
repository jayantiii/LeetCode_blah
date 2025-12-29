class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        graph = {i:[] for i in range(len(vals))}
        for u,v in edges:
            # Only consider neighbors with positive values
            #This is okay cause we dont need to traverse or anything
            if vals[v] > 0:
                graph[u].append(vals[v])
            if vals[u] > 0:
                graph[v].append(vals[u])

        maxsum = float("-inf") #dont intialise as zero

        for node in graph:
            graph[node].sort(reverse=True)
            nodesum = vals[node] + sum(graph[node][:k]) # add center val too
            maxsum = max(maxsum,nodesum)
        return maxsum


#Hint - You dont need to traverse the graph as such
#For each node, sort its neighbors in descending order and take k max valued neighbors.

# Sorting isn't "In-place": sorted(graph[node]) returns a new list; it doesn't modify the existing one. You need to use graph[node].sort() or reassign the variable.

#I tried doing like this - This inner loop not needed
        #  for neigh in graph[node]: #graph[node], not just node
        #         nodesum += vals[neigh]