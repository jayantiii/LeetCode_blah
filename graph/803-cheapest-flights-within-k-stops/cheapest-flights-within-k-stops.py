class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #cant use djistra algo easily cause given atmost k case
        # we will us bellman ford algo

        prices = [float('inf')]*n
        prices[src] = 0 #src to src is zero

        for i in range(k+1): #k+1 needed, simple observation
            pricestemp = prices.copy() #temp is needed so that IMPPPPP!!   
            #results for the current stop-count 
            for s, d, cost in flights:

                #if s can be reached from src then only
                if prices[s] == float('inf'):
                    continue # means the node cant be reached from our src
                #You should use OLD values to relax edges, # but you should COMPARE/WRITE into the NEW 
                # use OLD prices[s], update NEW pricestemp[d]
                if pricestemp[d] > prices[s] +cost : #pricestemp[s] and not prices[s]
                    pricestemp[d] = prices[s] +cost 

            prices = pricestemp
        return -1 if prices[dst] == float('inf') else prices[dst] 

##note - djistra cant deal with negative weights, bellmanford can

#My try, passed half cases but complex and wrong wrong
#cause you process newly discovered nodes inside the same stop-level

        # adj = {i:[] for i in range(n)}
        # for sr,to,price in flights:
        #     adj[sr].append([to,price]) # build adj list

        # cheapprices = [float('inf')]*n #array to store cheapest paths from srcnode to a node
        # cheapprices[src] = 0 # src nod eto src node is zero
        # q = deque([])
        # q.append(src)
        # stops = 0
        # while q and stops <= k:
        #     prices_temp = cheapprices.copy()
        #     for i in range(len(q)):
        #         src = q.popleft()   
        #         for neigh,price in adj[src]:
        #             if cheapprices[src] + price < prices_temp[neigh]:
        #                 prices_temp[neigh] = cheapprices[src] + price
        #             q.append(neigh)
        #     stops += 1
        #     cheapprices = prices_temp

        # if cheapprices[dst] != float('inf'):
        #     return cheapprices[dst]
        # else:
        #     return -1 





        
