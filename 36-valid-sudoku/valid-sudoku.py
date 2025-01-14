class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row  = defaultdict(set)
        col = defaultdict(set)
        mat  = defaultdict(set) # means any new key will be assigned an empty set

        for i in range(9): # its not in board, dont confuse
            for j in range(9) :
                if board[i][j] == ".": # dont forget to add this case
                    continue

                if(board[i][j] in row[i] or
                   board[i][j] in col[j] or
                   board[i][j] in mat[(i//3,j//3)] ):
                   return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    mat[(i//3,j//3)].add(board[i][j])
        return True # dont by mistakely put in for loop( indent imp!)
        