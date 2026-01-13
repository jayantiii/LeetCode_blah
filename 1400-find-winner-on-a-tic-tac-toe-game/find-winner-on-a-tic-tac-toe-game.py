class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        #Only when it reaches +3 (A) or -3 (B) do you have a win.
        hashmap = {i:0 for i in range(9)} # let x be +1, o -1
        
        for turn, (i,j) in enumerate(moves):
            val = 1 if turn % 2 == 0 else -1  # A:+1, B:-1

            lineids = [i,j+3] #lines to check

            if i==j:  # one diagonal
                lineids.append(7)

            if i + j == 2: #this logic!!
                lineids.append(8)

            for line in lineids:
                hashmap[line] += val
                if hashmap[line] == 3:
                    return "A"
                if hashmap[line] == -3:
                    return "B"

        if len(moves) == 9:
            return "Draw"

        return "Pending"


#-----without hashmap use below variables-------------------------------
        # rows = [0, 0, 0]
        # cols = [0, 0, 0]
        # diag = 0
        # anti = 0

# the hashmap stores a single integer per line that represents the net ownership of that line:

# line ids:
# rows: 0,1,2
# cols: 4,5,6  (4 + c)
# diag: 7
# anti: 8

