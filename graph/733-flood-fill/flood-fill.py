class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orgcolor = image[sr][sc]
        #very imp orelse if same, u will keep repainting forever 
        if orgcolor == color:
            return image

        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != orgcolor:
                return

            image[i][j] = color    
            dfs(i,j+1) #right
            dfs(i,j-1) #left
            dfs(i+1,j)#down
            dfs(i-1,j) #up

        dfs(sr,sc)
        return image

#IMP - If the new color equals the original color, the algorithm keeps repainting forever.
#ask this question, will it always be different color
        