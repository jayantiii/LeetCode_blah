class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda i : i[0]) # sort on start times

        for i in range(1, len(intervals)): # can start from 1
            # if start time of second meet is before end of first
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True

            
#Some clarify q's
# For empty input (no meetings), should we return true or false?
#If two meetings end and start at the same time, is that considered overlapping?
#are they sorted in any order
#Are the intervals inclusive or exclusive of endpoints?

#Bruetforce
#compare every meeting time to every other meeting time

        # for i in range(len(intervals)):
        # ##IMPPPPPP !! start from i +1, if start from i, will comapre itself
        #     for j in range(i+1,len(intervals)):
        #         onestart, oneend = intervals[i][0] ,intervals[i][1]

        #         twostart = intervals[j][0]
        #         twoend = intervals[j][1]
        #          #max(start_i, start_j) < min(end_i, end_j) - this should be - IMPPP
        #         if oneend > twostart and twoend > onestart:
        #             return False
        # return True