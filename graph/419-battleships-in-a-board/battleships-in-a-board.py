class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
#Understand the question
#can only be made of the shape 1 x k (1 row, k columns) or k x 1
#So every ship has exactly one unique “starting cell”.
        m = len(board)
        n = len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    #count only if starting point or top row/col
                    if (i==0 or board[i-1][j] == ".") and \
                    (j==0 or board[i][j-1] == "."):
                        count +=1

        return count

        