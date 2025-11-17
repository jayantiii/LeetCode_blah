class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i in range(len(intervals)):
        ##start from i +1, if start from i, will comapre itself
            for j in range(i+1,len(intervals)):
                onestart, oneend = intervals[i][0] ,intervals[i][1]

                twostart = intervals[j][0]
                twoend = intervals[j][1]
                 #max(start_i, start_j) < min(end_i, end_j) - this should be
                if oneend > twostart and twoend > onestart:
                    return False
        return True
                
        

#Some clarify q's
# For empty input (no meetings), should we return true or false?
#If two meetings end and start at the same time, is that considered overlapping?
#are they sorted in any order
#Are the intervals inclusive or exclusive of endpoints?

#Bruetforce
#compare every meeting time to every other meeting time