class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort & Greedy 
        #When two intervals overlap, we should remove the interval with the larger end time,  because it restricts the future choices more.
        intervals.sort(key = lambda i : i[0])
        count =0
        prevend = intervals[0][1] #first
        for i in range(1, len(intervals)):
            #Nooverlap, if start of second is more than prevend
            if intervals[i][0] >= prevend:
                 #if no overlap, just update prevend
                prevend =  intervals[i][1]             
            else: #overlap
                count +=1
                #need to save which end we keep
                prevend = min(intervals[i][1],prevend)
        return count


#see the logic when sorting by start, maybe thats why if sort by end is better


            






# Instead of “minimum intervals to remove,” think:
# “What is the maximum number of intervals I can keep so that they don’t overlap?”
# Then the answer = total_intervals - max_non_overlapping.
        