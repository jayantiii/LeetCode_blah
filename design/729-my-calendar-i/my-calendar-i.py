class Node(): #bst tree node!! Use this store events
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    # def insert(self,start,end) - can do this here to0

class MyCalendar:
    #  Your BST: checks only a single path down the tree ⇒ O(h) per book()
    def __init__(self):
        self.root = None
        
    def book(self, startTime: int, endTime: int) -> bool:
        newnode = Node(startTime, endTime)
        if self.root == None:
            self.root = newnode
            return True

        curr = self.root
        while curr:
            # New interval entirely before curr
            if endTime <= curr.start: #left tree
                if not curr.left:
                    curr.left = newnode
                    return True

                curr = curr.left

            # New interval entirely after curr
            elif startTime >= curr.end:
                if not curr.right: #update here itself in while not after while
                    curr.right = newnode
                    return True
                curr = curr.right

            # Overlap
            else:
                return False

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)


#---------------NOTES------------------------------------

#interesting - USE BST to store events

#Store the events as a sorted list of intervals. If none of the events conflict, then the new event can be added.

# In MyCalendar I (BST), you conceptually “insert at a leaf” (i.e., you keep walking left/right until you hit a None child, then attach the new interval there). You do not “insert in the middle” by splicing between two existing nodes.

#------------------------bruteforce, compare with all bookings-------------
    # def book(self, startTime: int, endTime: int) -> bool:
    #     # overlap exists iff max(s1, s2) < min(e1, e2) for half-open intervals
    #     for s, e in self.events:
    #         if max(s, startTime) < min(e, endTime):
    #             return False
    #     self.events.append((startTime, endTime))
    #     return True