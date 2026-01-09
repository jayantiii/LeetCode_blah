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


        
 #The idea is to know exactly, where to divide the order of books. Divide in such a way that the height per section is minimized leading to overall min height while maintaining the sum of thickness.               
    
#Order fixed means: within each shelf, books must appear in the same left-to-right order as the input.# But you still get to choose where to break shelves. That’s a “partition into contiguous groups” problem.

#Yes — cur_h is necessary for your “same shelf vs new shelf” DFS.
# Reason: the objective is sum of (max height on each shelf). While you’re filling a shelf, you must remember the current shelf’s max height, so that when you decide to start a new shelf you can add that height.

#------------My first try - wrong understanding of question-------------------------------
# I thought books width is given and its simple and no height given
# but i was wrong, books height and width both is given and read Q carefully!!
        