class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        visit = set() #store NUMBERS (1..9), not (i,j)
        skip = {
            (1,3):2,
            (4,6):5,
            (7,9):8,
            (1,7):4,
            (2,8):5,
            (3,9):6,
            (1,9):5,
            (3,7):5

            #reverse (i,j) and (j,i) both will have same values
            #so consider that while dfs code
        }
   
        def dfs(i,j,length): #return count starting from this cell!    
            num = mat[i][j]  
            if mat[i][j] in visit:
                return 0

            if length > n:
                return 0

            visit.add(mat[i][j])
        
            count = 0
            if m <= length <= n:
                count = 1
            else:
                count = 0
            
            for ni in range(3): #next number
                for nj in range(3):
                    if mat[ni][nj] in visit: #no repeatations
                        continue

                    num = mat[i][j]
                    nxt = mat[ni][nj]

                    mid = skip.get((num, nxt), skip.get((nxt, num), 0))
                    if mid != 0 and mid not in visit:
                        continue

                    count += dfs(ni,nj,length+1)

            visit.remove(num)   # BACKTRACK needed
            return count

        totalcount = 0
        for i in range(3):
            for j in range(3):
            #from each cell start and do dfs!
                totalcount += dfs(i,j,1)
                visit.clear()
            
        return totalcount
                   
        
#Idea
#do dfs from each cell
#precompute a small skip[a][b]=mid table (9x9). Then during backtracking/DFS you can test a move in O(1): so mid is the middle point of a,b if exists

#-----------------------------------------Question-------------------------------------
#if i find count for one corner, will count for all 4 corners be same
# Yes: by symmetry, the count starting from any corner is the same.
# Corners: {1,3,7,9} all equivalent → count(corner) same.
# Edges: {2,4,6,8} all equivalent → count(edge) same.
# Center: {5} unique.

# m <size <= n
# Dont write --> if length > n-m: return 0  --- in dfs is this not right
# n - m is also not the right cutoff.
# n - m is just a range width, not a length limit.
# Correct rule:
# Stop when length > n.

# visit.remove(num) is needed because visit is shared across all recursive calls. DFS is exploring many different paths; when you finish exploring paths that start with a certain prefix, you must undo the “I visited this dot” mark before you try a different branch.

#-----------------------------Some confusions--------------------------------
# Key idea:
# dfs(state) should return: "how many VALID patterns exist from this state onward"
# In DFS, you are at some current length `length`.
# - If length is already within [m, n], the CURRENT path is a valid pattern -> contributes +1.
# - If length < m, the CURRENT path is NOT valid yet -> contributes +0.
# - Regardless, you can keep extending (until length > n).

# WRONG:
#   count += 1 + dfs(next, length+1)
# Because that "1" is saying:
#   "as soon as I move to next, I always created a valid pattern"
# But validity depends on new_len = length+1 being >= m.

# Example:
#   m=4, n=9
#   current length = 2  (path has 2 dots)
#   move to next -> new_len = 3
#   Is a length-3 pattern valid? NO, because 3 < 4
#
# So adding "+1" here would count an INVALID pattern.
# Correct:
#   new_len = length + 1
#   add = 1 if m <= new_len <= n else 0
#   count += add + dfs(next, new_len)
#
# Or (cleaner):
#   count = 1 if m <= length <= n else 0        # count the CURRENT path if valid
#   for each valid next:
#       count += dfs(next, length+1)            # children counts handle their own "is valid" check
