class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
    
        #Do not return anything, modify matrix in-place instead.
        '''observe the pattern in input and output matrix, this logic hard, see notes video '''
        l,r = 0, len(matrix) -1
        while l<r :
            for i in range(r-l):
                t,b = l,r          #top bottom left right pointers
                topleft_temp = matrix[t][l+i] # save topleft value
                matrix[t][l+i] = matrix[b-i][l] #move bl to tl
                matrix[b-i][l] = matrix[b][r-i] #move br to bl
                matrix[b][r-i] = matrix[t+i][r] # move tr to br
                matrix[t+i][r] = topleft_temp  #move tl to tr
            r-=1
            l+=1
            
''' simpler method  --> transpose then reverse           
        n = len(matrix)
        for i in range(n): # transpose
            for j in range(i,n): # use (i,n) not (n) to prevent overwriting - tricky
                # we need to use temp here cause we are replacing in the same 2d array
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i] # only this line would be enough,if new array was used for result.
                matrix[j][i] = temp
        
        for row in matrix:
            row.reverse()
        # matrix = list(map(lambda x: x[::-1],matrix)) -- a method to reverse
 '''       
        
        