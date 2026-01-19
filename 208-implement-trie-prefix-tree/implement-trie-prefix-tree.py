class Trie:

    def __init__(self):
        self.children = {}
        self.isword = False
        

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr = curr.children[c]
        curr.isword = True
        
    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isword
        
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
            

    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#--------------------NOTES-----------------
#For any node, isword answers:
#“Is the prefix up to this node a complete stored word?”

# What children actually means
# children: dict[char, TrieNode]

# So if you’re at some node and the next character is 't', you take:
# next_node = node.children['t']

#-----------Example, bat and ball-----------------
# #root
#  └─ 'b' -> node_b
#         └─ 'a' -> node_ba
#                ├─ 't' -> node_bat   (isword=True)
#                └─ 'l' -> node_bal
#                       └─ 'l' -> node_ball (isword=True)

