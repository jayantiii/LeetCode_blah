class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        totalgas = 0
        startpoint = 0
        for i in range(len(gas)):
            totalgas += gas[i] - cost[i]
            if totalgas < 0:
                #restart startpoint
                startpoint = i+1
                totalgas = 0 #start with empty
        return startpoint

#Greedy problem

#Notice - sum(gas) >= sum(cost) to complete a loop !1! IMP point!!