class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort by x increasing; if same x, by y decreasing.
        # This prevents "same-x" points from creating fake rectangles and keeps logic valid.
        points = sorted(points, key=lambda p: (p[0], -p[1]))
        count = 0
        for i in range(len(points)): #upper left
            x1,y1 = points[i][0], points[i][1]
            best_y2 = float("-inf")  # best (= highest) y2 seen so far with y2 <= y1

            for j in range(i+1,len(points)): #and lower-right
                x2,y2 = points[j][0], points[j][1]

                # must be below/at y1 to be a lower-right
                if y2 <= y1 and y2 > best_y2:
                    count += 1
                    best_y2 = y2

        return count

#Bruetfroce is to have 3rd inner loop to check if a point there is the rect formed.

     



        

#We can enumerate all the upper-left and lower-right corners.