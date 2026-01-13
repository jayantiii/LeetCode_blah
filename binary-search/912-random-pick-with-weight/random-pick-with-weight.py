class Solution:

    def __init__(self, w: List[int]):
        self.rangemax = -1 #last number in ranges
        self.ranges = [] # array of same size as w

        for i in range(len(w)):
            self.ranges.append(self.rangemax + w[i]) #just append
            self.rangemax += w[i]

    # we dont find the exact number, but number which is less than pickr
    # thus we dont have a condition called if mid == pickr
    def binarysearch(self, pickr):
        l,r = 0,len(self.ranges)-1  #cant access w here, its only to init
        while l<r: # no equal sign needed
            mid = (l+r)//2
            if self.ranges[mid] < pickr:
                l = mid+1
            else:
                r = mid   #mid not +1
        return l  #think to figure out

#1 // 2 ans is 0 
#[1,200,205,207] - 198 - return 1
        
    def pickIndex(self) -> int:
        pickr = random.randint(0, self.rangemax)
        #now we need to find which index in ranges is the picked range present
        #Use Binary search, as ranges will be in increasing order
        index = self.binarysearch(pickr)
        return index


#Dont forget self. everywhere and also pass it in binarysearch function
        
#Idea
# inp - [1,3] # - here the idea is to draw them on number line
# - [1,3,3,3] # - but if weights are more, then it will become very big array
# - so rather we can store intervals
# - so store ranges [1,4] 
#then do binary search to find the picked range

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()