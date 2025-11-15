class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Bruteforce - Dfs on each cell
        # Optimal -reverse the condition as we start dfs from ocean side and not cell side
        rows = len(heights)
        cols = len(heights[0])
        result = []
        pac = set()
        atl = set()

        def dfs(r,c,ocean, prevH):
            #Base
            if r < 0 or r>=rows or c<0 or c >=cols or (r,c) in ocean or heights[r][c] <prevH:
                return

            ocean.add((r,c))
            dfs(r+1,c,ocean,heights[r][c])
            dfs(r-1,c, ocean, heights[r][c])
            dfs(r,c+1, ocean, heights[r][c])
            dfs(r,c-1, ocean, heights[r][c])

        for c in range(cols):        
            dfs(0,c, pac,-1) # first row
            dfs(rows-1,c, atl,-1) # last row

        for r in range(rows):        
            dfs(r,0, pac,-1) # first col
            dfs(r,cols-1, atl,-1) # last col

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])
        return result

        