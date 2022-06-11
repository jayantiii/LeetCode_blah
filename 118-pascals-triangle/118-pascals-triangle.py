class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]  # cool line - open notes
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j] + pascal[i-1][j-1]
        return pascal
   
        

# My approach - passed all cases but can be made more efficient

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         if numRows == 1:return [[1]]
#         mat = [[1],[1,1]]
#         if numRows == 2:return mat
#         for i in range(2,numRows):
#             temp = [1,1]
#             prev = mat[i-1]
           
#             for j in range(i-1):
#                 temp.insert(j+1,prev[j]+prev[j+1])
#             mat.append(temp)
#         return mat