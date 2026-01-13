class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        while matrix:
            #first row
            firstrow = matrix.pop(0) 
            for x in firstrow:
                res.append(x)

            #last col
            if not matrix or not matrix[0]:break
            for row in matrix:
                lastcol = row.pop(-1)
                res.append(lastcol)
            
            if not matrix or not matrix[0]:break
            #lastrow, but in reverse!!
            lastrow = matrix.pop(-1)
            for x in range(len(lastrow)-1,-1,-1): #reverse ok!
                res.append(lastrow[x])
            
            if not matrix or not matrix[0]:break
            #firstcol in reverse!! dont forget reverse
            for row in matrix[::-1]:
                firstcol = row.pop(0)
                res.append(firstcol)

        return res


#remove the respected rows and columns as we traverse
#We can then make while loop of repeated such steps

        