class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #find one cell with land and then do dfs from there, O(rows × cols)
        # add to perimiter only when water encountered
        perimeter = 0
        def dfs(m: int,n:int):
            nonlocal perimeter  #needed if trying to update inside
            #when you step off grid from land, that side is part of the perimeter
            if m < 0 or m >=len(grid) or n < 0 or n >= len(grid[0]) or grid[m][n] == 0:
                perimeter +=1
                return      
            # already visited land → no extra perimeter from this cell
            if grid[m][n] == -1:
                return
            # mark current land cell as visited
            grid[m][n] = -1

            dfs(m,n+1)
            dfs(m,n-1)
            dfs(m-1,n)
            dfs(m+1,n)
                
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:  #0 and 1 are not strings here, pay attention
                    dfsres = dfs(m,n)
                    break

        return perimeter

# Also its better not to use nonlocal so do something like make dfs return perimeter
#    return (
#                 dfs(r+1, c) +
#                 dfs(r-1, c) +
#                 dfs(r, c+1) +
#                 dfs(r, c-1)
#             )

#Without recursion soln, O(rows × cols),
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     perimeter = 0

    #     for r in range(rows):
    #         for c in range(cols):
    #             if grid[r][c] == 1:
    #                 # each land cell contributes 4 sides initially
    #                 perimeter += 4

    #1 shared edge reduces perimeter by 2
    # you can use anypair of opp directions but not all

    #                 # if the cell above is also land, we remove 2 (shared edge)
    #                 if r > 0 and grid[r - 1][c] == 1:
    #                     perimeter -= 2

    #                 # if the cell to the left is also land, we remove 2 (shared edge)
    #                 if c > 0 and grid[r][c - 1] == 1:
    #                     perimeter -= 2

    #     return perimeter
        