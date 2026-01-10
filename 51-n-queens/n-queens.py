class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        negdiag = set() #(r-c)
        posdiag =set() #(r+c)
        board = [["."]*n for i in range(n)]
        res = []

        def backtrack(r):#one queen each row has n cell choicess
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

# Backtracking row-by-row: in each row r, try every column c where no earlier queen attacks it (tracked by cols, posdiag=r+c, negdiag=r-c).
# Place "Q", recurse to r+1, then undo (remove from sets + reset ".") to explore the next option; when r==n, record the board as one valid solution.

# Time:
# - We place exactly 1 queen per row.
# - Row 0 has up to n choices, row 1 up to (n-1), row 2 up to (n-2), ...
#   => about n * (n-1) * (n-2) * ... * 1 = n! possibilities in the worst case
# - Each "is this safe?" check is O(1) because cols/diags are sets
# - When we find a full solution, we convert the board to strings: O(n^2) per solution
# => Worst-case: O(n!) for the search (+ output building cost)

# Space:
# - board is n x n => O(n^2)
# - sets + recursion depth are size O(n)
# => Total extra space: O(n^2)

        