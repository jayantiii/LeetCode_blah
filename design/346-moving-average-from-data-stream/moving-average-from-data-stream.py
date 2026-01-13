class MovingAverage:
    """
    Maintain a sliding window of at most `size` values and a running sum.

    next(val):
      - push val into window
      - if window too big, pop left and subtract it from sum
      - average = sum / len(window)
    """

    def __init__(self, size: int):
        self.size = size     
        self.runningsum = 0
        self.q = deque() #queue is window!

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            firstele = self.q.popleft()
            self.runningsum -= firstele

        self.q.append(val)
        self.runningsum += val #dont forget

        return self.runningsum / len(self.q)
        

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)