class Solution:
    def knightDialer(self, n: int) -> int:

        mat = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),
                       (1,-2),(1,2),(2,-1),(2,1)]

        @lru_cache(None)
        def dfs(i,j,length):
            if i < 0 or i >= 4 or j <0 or j >= 3:
                return 0
            
            if mat[i][j] == "*" or mat[i][j] == "#":
                return 0

            if length == n-1:
                return 1

            count = 0
            for x,y in directions:
                count += dfs(i+x,j+y,length+1)

            return count



        total = 0
        for i in range(4):
            for j in range(3):
                if isinstance(mat[i][j], int):
                    count = dfs(i,j,0)
                    total += count

        return total % (10**9 +7)
        

# If you start with dfs(i,j,0), then base should be length == n-1 (or start at 1 and use length == n).

#In Python, .isdigit() is a string method. An int object simply doesn’t have that method.