class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if target <= row[-1]: # dont forget =
                return target in row
            else:
                continue
        return False
    
        