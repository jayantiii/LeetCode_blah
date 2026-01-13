# later try this in binary serach way
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]:
                return target in row
        return False

       
        
# My approach - passes all cases but can be made more effiecient        
#         m = len(matrix)
#         n = len(matrix[0])
#         i = 0
#         while(i < m):
        
#             if target <= matrix[i][n-1]:
#                 if target in matrix[i]:
#                     return True
#                 else:
#                     return False
                
#             else:
#                 i=i+1
        
        
        
        
        
        
        
        
        
    