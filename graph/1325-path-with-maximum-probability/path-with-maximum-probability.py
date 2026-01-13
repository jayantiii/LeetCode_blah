class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
# use djistra's, instead of minimising distance, maximise probab, so use max heap# we dont have maxheap but maybe add negative values and use minheap
        adj = {i:[] for i in range(n)}
        for i in range(len(edges)):
            u,v = edges[i]
            adj[u].append([v,succProb[i]])
            adj[v].append([u, succProb[i]]) #both sides

        #BFS #(probab, node) #priority queue
        #here prob is of reaching that node and -1 here makes it max heap
        pq = [(-1,start_node)] 
        visit = set()
        while pq:
            prob, node = heapq.heappop(pq) # pop min, means pop max probab, kinda like greedy
            visit.add(node)
            if node == end_node:
                return prob *-1 #return the actual

            for neigh, neighprob in adj[node]:
                totprob = neighprob * prob #dont need to do minus here
                if neigh not in visit: 
                    heapq.heappush(pq,(totprob, neigh)) #syntax
                # need to push even if it in heap already, cause there maybe better
        return 0





        






    #total probab sumt to 1 and never more than 1
        