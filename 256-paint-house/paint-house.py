class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #r,b,g
    #     #Create a dp matrix with (nx3) and fill row wise
    #      0 1 2
    # h1  17 2 17
    # h2.  18 35 7
    # h3   21. 10 

        # Bottom up approach
        prevhouse = [0,0,0]
 
        for i in range(0,len(costs)):
            house0 = costs[i][0] + min(prevhouse[1],prevhouse[2])
            house1 = costs[i][1] + min(prevhouse[0],prevhouse[2])
            house2 = costs[i][2] + min(prevhouse[0],prevhouse[1])

            prevhouse = [house0,house1, house2]
        
        return min(prevhouse)


        #BRUTEFORCE - You start from house i and try every allowed colour. For each colour, you recursively compute the cost of painting the next house with the constraint that no two adjacent houses share a colour.
# Time complexity = O(3^n) because for every house you have 3 choices.
        # n = len(costs)

        # # dfs(i, prev) returns the minimum cost from house i to end
        # # given that previous house was painted with color 'prev'
        # def dfs(i, prev):
        #     # Base case: painted all houses
        #     if i == n:
        #         return 0

        #     best = float('inf')

        #     # Try all 3 colours
        #     for color in range(3):
        #         # Can't use same colour as previous house
        #         if color != prev:
        #             cost_now = costs[i][color]
        #             # Recursively compute cost of painting next houses
        #             total_cost = cost_now + dfs(i + 1, color)
        #             best = min(best, total_cost)

        #     return best

        # # Start at house 0 with no previous color
        # return dfs(0, -1)
        
#I started this try but it wont lead anywhere much
#    n = len(costs)
#         if !costs: return 0
#         if n ==1:
#             return min(costs[0])

#         firsthouse = min(costs[0])
#         firsthousecolor = min(cos)
#         prevhousecolor = 