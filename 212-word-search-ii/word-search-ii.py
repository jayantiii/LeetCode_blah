class TrieNode:
    def __init__(self):
        self.isword = False #children (edges to next letters)
        self.children = {} ## char -> TrieNode

    def addword(self,word): #Interesting!1
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c] 
        curr.isword = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        root = TrieNode()
        #Make a trie of words
        for word in words:
            root.addword(word)

        res = []
        visit = set ()
        def dfs(i,j,node,string):
            if i < 0 or j < 0 or i >= m or j >=n:
                return
            if (i,j) in visit or board[i][j] not in node.children  :
                return
            
            visit.add((i,j))
            c =  board[i][j]

            nextnode = node.children[c]
            if nextnode.isword:
                res.append(string + c)
            dfs(i+1,j,node.children[c],string + c)
            dfs(i-1,j,node.children[c],string + c)
            dfs(i,j+1,node.children[c],string + c)
            dfs(i,j-1,node.children[c],string + c)

            visit.remove((i,j))

        for i in range(m):
            for j in range(n):
                dfs(i,j,root,"") #see if any  word from here

        return list(set(res))

#----------------------
# cur = self means: “make a second reference to the same node, 
#so I can move cur while keeping self conceptually ‘the root’.”

# In that Word Search II pattern, dfs(r, c, node, word) is carrying two pieces of state while you walk the grid:
# node: where you are in the trie (which prefixes are still possible)
# word: the string you’ve built so far along the board path