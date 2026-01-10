class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negdiag = set() #(r-c)
        posdiag =set() #(r+c)
        board = [["."]*n for i in range(n)]
        res = []

        def backtrack(r):
            if r == n: #last row
                b = ["".join(row) for row in board]
                res.append(b)
                return

            for c in range(n):
                if c in cols or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                board[r][c] = "Q" 

                cols.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)

                backtrack(r+1)

                board[r][c] = "." 
                cols.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
        
        backtrack(0)

        return res

        