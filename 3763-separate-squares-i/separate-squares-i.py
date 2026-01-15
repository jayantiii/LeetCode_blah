class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        #Inetresting Idea - Binary search on the y axis
        precision = 10 ** (-5)
        ymin = min(y for _, y, _ in squares)
        ymax = max(y + l for _, y, l in squares)

        totalarea = 0
        for x,y,l in squares:
            totalarea += l*l
            
        # IMP - I got confused!! area below is more then return true
        def areabelowmid(yline):
            area = 0
            for x,y,l in squares:
                ytop = y + l
                if y <=  yline and ytop <= yline: #complete below
                    area += l*l

                elif y < yline and ytop > yline: # half in the line
                    overlap = l * (yline-y)
                    area+= overlap

            if totalarea/2  <= area:
                return True
            return False

                
        l,r = ymin, ymax
        miny = float('inf')
        #Condition!!
        while r - l >= precision: #keep shrinking until it’s small enough.
            mid = (l+r)/2
            if areabelowmid(mid): #area below is more or eq
                r = mid
            else: 
                l = mid #area is less

        return r
        #You return the boundary that you’ve been keeping “correct by definition.”

#IMP NOTES!!
# With floats, you don’t have a “next value” like mid+1 / mid-1, and you can’t rely on ever hitting the exact answer. So the implementation changes:

# In float binary search, there are infinitely many values between l and r, so +1/-1 is meaningless and can skip the answer. You must do l = mid or r = mid and stop when the gap r-l is tiny.

# Also, because floats rarely hit exact equality, you don’t try area == half. Instead you search for the boundary using area >= half, and the “precision” comes from how small you make r - l.

#--------------------Why return "r" here---------------------------
# In your implementation you maintain this invariant:
# l is on the False side: area_below(l) < half (not enough)
# r is on the True side: area_below(r) >= half (enough)
# So at the end:
# l is still not enough
# r is still enough
# the answer you want is the smallest y that is enough → that’s r

# Return l when you are solving the other boundary:
# largest y such that area_below(y) <= half (the “last OK” point)