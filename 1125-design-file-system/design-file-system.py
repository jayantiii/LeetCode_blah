class Node: #Node(nodes of tree), not Class Tree
    def __init__(self):
        self.children = {}
        self.value = None


class FileSystem:
    def __init__(self):
        self.root= Node() #represents "/""
        
    def createPath(self, path: str, value: int) -> bool:
        # invalid
        if not path or path == "/":
            return False
        #new leaf
        newnode = Node()
        newnode.value = value

        parts = path.split("/")[1:] # since leading "" this will be in array
        parent = self.root
        newfile = parts[-1]

        for name in parts[:-1]:
            if name not in parent.children:
                return False
            parent = parent.children[name]

        leaf= parts[-1]
        if leaf in parent.children:   # path already exists, no need to self.get(path) 
            return False
        parent.children[leaf] = newnode
        return True
 

    def get(self, path: str) -> int: #no recursion needed
        if not path or path == "/":
            return -1

        parts = [p for p in path.split("/") if p]  # FIX, since leading "" this will be in array
        curr = self.root
        for name in parts:
            if name not in curr.children:
                return -1
            curr = curr.children[name]

        return -1 if curr.value is None else curr.value #dont direct return
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

#What if you think of a tree hierarchy for the files?.#
#A path is a node in the tree.
#Use a hash table to store the valid paths along with their values.

##--------------------- Dict method, no node class ------------------------------
# class FileSystem(object):
#     def __init__(self):
#         self.path2value = defaultdict(int)
#         self.path2value[''] = -1

#     def createPath(self, path, value):
#         dirs = path.split('/')
#         parent = '/'.join(dirs[:-1])
#         if path in self.path2value or parent not in self.path2value:
#             return False
#         self.path2value[path] = value
#         return True

#     def get(self, path):
#         if path in self.path2value:
#             return self.path2value[path]
#         return -1
#----------------------Example node--------------------------
#   createPath("/a",   1)
#   createPath("/a/b", 2)
#   createPath("/a/c", 3)
#   createPath("/x",   8)
#   createPath("/x/y", 9)

# Tree (root represents "/"):

#             "/"  (root, value=None)
#              |
#       -----------------
#       |               |
#    "a" (1)         "x" (8)
#       |               |
#    --------         "y" (9)
#    |      |
#  "b"(2) "c"(3)

# Edges are folder names.
# Node value is the integer stored by createPath(path, value).
# get("/a/b") -> 2
# get("/x")   -> 8
# get("/z")   -> -1 (missing)

# Think of each node as:
#   Node.value    -> int | None
#   Node.children -> dict[str, Node]
#
# # Then the tree you drew is stored like this (conceptually):
# root.value = None
# root.children = {
#     "a": Node(value=1, children={
#         "b": Node(value=2, children={}),
#         "c": Node(value=3, children={}),
#     }),
#     "x": Node(value=8, children={
#         "y": Node(value=9, children={}),
#     }),
# }
# # So lookups are just chained hashmap accesses:
# # get("/a/b"):
# #   cur = root
# #   cur = cur.children["a"]   -> Node(value=1, ...)
# #   cur = cur.children["b"]   -> Node(value=2, ...)
# #   return cur.value          -> 2
