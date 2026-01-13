class Logger:

    def __init__(self):
        self.hashmap = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.hashmap:
            self.hashmap[message] = timestamp
            return True
        else:
            if timestamp - self.hashmap[message] >= 10:
                self.hashmap[message] = timestamp
                return True
        return False
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

# #-------------- follow up question for this ------------------------
# Question: If duplicate messages come within a 10secs window then discard previous and current Message.
# The solution for this question will be given using Linked list and a MAP. A map to store the last reference of the message and linked list to print those messages later. This question has been recently asked in FAANG.

# -- Answer-- follow up---
#  - So the only correct approach is: delay printing by 10 seconds. If a duplicate arrives before the delay expires, you cancel the pending print (discard “previous”) and also discard the current one.

# Data structure
# HashMap pending: message -> node (so you can delete a pending message in O(1))
# Doubly linked list (time ordered): nodes are “candidates to print later”, each with expire = timestamp + 10
# HashMap last_seen: message -> last timestamp (to detect “duplicate within 10s”)
# Operations (timestamps are non-decreasing)
# When you receive (t, msg):
# Flush: while list head has expire <= t, pop it and “print” it (it survived 10 seconds without duplicates).
# If msg seen within 10 seconds (t - last_seen[msg] < 10):
# If msg is pending, remove its node from the list (discard previous)
# Do not add current message (discard current)
# Else: add msg as a pending node with expire = t + 10

#Example of node
    # def __init__(self) -> None:
    #     self.pending: Dict[str, Node] = {}      # msg -> node in DLL (if pending)
    #     self.last_seen: Dict[str, int] = {}     # msg -> last timestamp seen (even if discarded)

    #     # sentinel DLL: head <-> ... <-> tail
    #     self.head = Node("__HEAD__", -1)
    #     self.tail = Node("__TAIL__", -1)
    #     self.head.next = self.tail
    #     self.tail.prev = self.head