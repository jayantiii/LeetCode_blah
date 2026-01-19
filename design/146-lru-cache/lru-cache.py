class Node: #Doubly linked list
    def __init__(self,key,val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:
    def __init__(self, capacity: int):
        self.hashmap = {} #size of hashmap dont need to exceed capacity
        self.left = Node(0,0) #least used
        self.right = Node(0,0) # most used
        self.cap = capacity

        self.left.next = self.right #wire them
        self.right.prev = self.left

        #so we insert nodes in mid of left and right dummy nodes

    def remove(self,node):
        prevnode = node.prev
        nxtnode = node.next
        prevnode.next = nxtnode
        nxtnode.prev = prevnode

    def insert(self,node):
        currmost = self.right.prev
        currmost.next = node
        node.prev = currmost
        self.right.prev = node
        node.next = self.right

  
    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1  
        node = self.hashmap[key]
        self.remove(node) #remove node from its curr location
        self.insert(node) #Update the most recently used

        return node.val

    def put(self, key: int, value: int) -> None:

        # Imp -> If key already exists, you shouldn’t evict.
        if  key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node) #remove node from its curr location
            self.insert(node) #Update the most recently used

        else:  
            if len(self.hashmap) == self.cap: #evict 
                lru = self.left.next
                self.remove(lru)
                del self.hashmap[lru.key]

            node = Node(key,value)
            self.hashmap[key] = node #store
           
            #Update the most recently used
            self.insert(node)

        return


#How to get O(1): HashMap + Doubly Linked List#

#In an LRUCache, the node must let you remove the correct entry from the hashmap when you evict (or move) a node. For that you need the key.

#Use OrderedDict (built-in in Python)
#OrderedDict is a subclass of Python’s built-in dictionary dict that remembers the order in which keys are inserted. # Internally, OrderedDict already keeps a doubly linked list for you.

# from collections import OrderedDict

# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cache = OrderedDict()
#         self.capacity = capacity

#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         # mark key as recently used
#         self.cache.move_to_end(key)
#         return self.cache[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)   # remove least recently used