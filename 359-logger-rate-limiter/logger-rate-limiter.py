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

# #-------------- follow up question for this, Space Optimization ----------------------
# Question: If duplicate messages come within a 10secs window then discard previous and current Message.
# The solution for this question will be given using Linked list and a MAP. A map to store the last reference of the message and linked list to print those messages later. This question has been recently asked in FAANG.