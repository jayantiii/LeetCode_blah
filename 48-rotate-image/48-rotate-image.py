class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #observe the pattern in input and output matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i,n): # use (i,n) not (n) to prevent overwriting - tricky
                # we need to use temp here cause we are replacing in the same 2d array
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i] # only this line would be enough,if new array was used for result.
                matrix[j][i] = temp
        
        for row in matrix:
            row.reverse()
        matrix = list(map(lambda x: x[::-1],matrix))
        
        