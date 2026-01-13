class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c: return mat
        newmat = []
        oneD_mat = [ i for e in mat for i in e]
        i =0
        for i in range(0,m*n,c): # better approach!
            newmat.append(oneD_mat[i:i+c])
       #  can replace above for loop by this below line
       #newmat = [ flatten_array[ y*c : y*c+c ] for y in range(r) ]
        return newmat
    
# My first approach - more time
    
#        m = len(mat)
#         n = len(mat[0])
#         if m*n != r*c: return mat
#         newmat = []
#         oneD_mat = [ i for e in mat for i in e]
#         i =0
#         for row in range(r):
#             temp =[]
#             for col in range(c):
#                 temp.append( oneD_mat[i])
#                 i+=1
#             newmat.append(temp)
            
#         return newmat
            