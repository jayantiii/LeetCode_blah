class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        #Kind of like greedy
        n = len(rooks)
        rooks.sort(key = lambda x:x[0])
        rowmoves = 0
        rownumber = 0
        for x,y in rooks:
            rowmoves = rowmoves + abs(x-rownumber)
            rownumber+=1   

        rooks.sort(key = lambda x:x[1]) 
        colmoves = 0
        colnumber = 0
        for x,y in rooks:
            colmoves = colmoves + abs(y-colnumber)
            colnumber+=1

        return  rowmoves + colmoves

#Obeserve that, rooks should occupy the diagonals
#mn rooks in nXn board, so every row and coln is bound to have one rook exact

#First, distribute the rooks in individual rows.
# You can do this by sorting all rooks by their rows. Then assign the first one to the first row, the second one to the second row, and so on.
#After you've distributed rooks across all rows, now do the same for columns.

#-----------------Clean same code------------------
#  n = len(rooks)

#         xs = sorted(x for x, _ in rooks)
#         ys = sorted(y for _, y in rooks)

#         # target rows/cols are 0..n-1
#         row_moves = sum(abs(xs[i] - i) for i in range(n))
#         col_moves = sum(abs(ys[i] - i) for i in range(n))

#         return row_moves + col_moves
