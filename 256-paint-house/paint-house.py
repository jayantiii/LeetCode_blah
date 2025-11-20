class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #r,b,g
    #     #Create a dp matrix with (nx3) and fill row wise
    #      0 1 2
    # h1  17 2 17
    # h2.  18 35 7
    # h3   21. 10 

        prevhouse = [0,0,0]
 
        for i in range(0,len(costs)):
            house0 = costs[i][0] + min(prevhouse[1],prevhouse[2])
            house1 = costs[i][1] + min(prevhouse[0],prevhouse[2])
            house2 = costs[i][2] + min(prevhouse[0],prevhouse[1])

            prevhouse = [house0,house1, house2]
        
        return min(prevhouse)


        


        

#I started this try but it wont lead anywhere much
#    n = len(costs)
#         if !costs: return 0
#         if n ==1:
#             return min(costs[0])

#         firsthouse = min(costs[0])
#         firsthousecolor = min(cos)
#         prevhousecolor = 