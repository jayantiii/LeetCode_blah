class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        @lru_cache(None)
        def backtrack(i,width,currh): #return min height
            if i == len(books):
                return currh  # pay height of the last (current) shelf

            #next level
            w , bookheight = books[i][0], books[i][1]
            nxt = currh + backtrack(i+1,shelfWidth - w,bookheight) #reset width, height

            #same level
            same = float("inf")
            #check if enough width is remaining
            if width >= books[i][0]:
                currh = max(currh, books[i][1])
                same = backtrack(i+1, width - books[i][0],currh)

            return min(same, nxt)


        return backtrack(0, shelfWidth,0)

# Your 3-param version (backtrack(i, width, currh)):
#   Time:  O(n^2 * W)
#   Space: O(n^2 * W)
#
# Standard dfs(i) / dp[i] version:
#   Time:  O(n^2)
#   Space: O(n)
        
 #The idea is to know exactly, where to divide the order of books. Divide in such a way that the height per section is minimized leading to overall min height while maintaining the sum of thickness.               
    
#Order fixed means: within each shelf, books must appear in the same left-to-right order as the input.# But you still get to choose where to break shelves. That’s a “partition into contiguous groups” problem.

#Yes — cur_h is necessary for your “same shelf vs new shelf” DFS.
# Reason: the objective is sum of (max height on each shelf). While you’re filling a shelf, you must remember the current shelf’s max height, so that when you decide to start a new shelf you can add that height.

# -------------DP------------------------------------------------------------------
# DP definition:
# - dp[i] = minimum total height to place the first i books (books[0 .. i-1]).
# - Base: dp[0] = 0  (no books => 0 height)

# How to fill the table:
# - Compute dp from left to right: i = 1..n
# - For each i, try all ways to make the LAST shelf:
#     last shelf = books[j .. i-1] for j = i-1 down to 0
#   while keeping total thickness <= shelfWidth.
# - Maintain running:
#     width   = sum(thickness of books[j..i-1])
#     shelf_h = max(height of books[j..i-1])
# - Transition:
#     dp[i] = min(dp[i], dp[j] + shelf_h)
# - Answer: dp[n]

#--------------- Backtrack with only one param---------------------------------------------

#  @lru_cache(None)
#         def dfs(i: int) -> int:
#             if i == n:
#                 return 0

#             width = 0
#             shelf_h = 0
#             best = math.inf

#             # put books[i..j] on the same shelf
#             for j in range(i, n):
#                 t, h = books[j]
#                 width += t
#                 if width > shelfWidth:
#                     break
#                 shelf_h = max(shelf_h, h)
#                 best = min(best, shelf_h + dfs(j + 1)) #means start next shelf at j+1!!

#             return best

#         return dfs(0)

#------------My first try - wrong understanding of question-------------------------------
# I thought books width is given and its simple and no height given
# but i was wrong, books height and width both is given and read Q carefully!!
        