class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0]) # sort by start
        res = [intervals[0]]
        for i in range(1,len(intervals)):
            lastres = res[-1][1]
            if lastres >= intervals[i][0]: #if lastres end more than start of interval
                res[-1][1] = max(intervals[i][1],  res[-1][1]) #update res
            else:
                res.append(intervals[i])
        return res

        
# [[1,3],[2,6],[8,10],[15,18]]
# if start of second < end of first
# [[1,6]]

#   i did this, and has lot of issuses
#yoou’re only ever comparing pairwise neighbors, not maintaining merged ranges
#You ignore non-overlapping intervals completely
#  res = []
#         for i in range(1,len(intervals)):
#             if intervals[i][0] < intervals[i-1][1]: #if start of second < end of first
#                 res.append([intervals[i-1][0], intervals[i][1]])


#         return res