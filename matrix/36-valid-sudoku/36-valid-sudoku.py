class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: # O(9*9)
        

        # hash set for each row in the grid
        # hash set for each col in the grid
        # hash set for each 3x3 box in grid
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)
        
    # in the first 2 dict , we keep row and col no. as key and values will be a set of numbers.
    #in last dict, 
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".": 
                    continue
                if(
                   board[i][j] in row[i] or
                   board[i][j] in col[j] or
                   board[i][j] in box[(i//3,j//3)]
                ):
                    return False

                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i//3,j//3)].add(board[i][j])
        return True
                                                               
                    
                   
                
        
        
        
      
        