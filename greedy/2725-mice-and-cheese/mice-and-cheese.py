class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        #Looks like DP, but it is greedy!!
        mouse2 = sum(reward2)

        diff =[(reward1[i] - reward2[i]) for i in range(len(reward1))]
        diff.sort()  
        maxsum =  0
        for i in range(len(reward1)-k,len(reward1)):
            maxsum = maxsum + diff[i]
        return mouse2 + maxsum
    
# Imagine at first that the second mouse eats all the cheese, then we should choose k types of cheese with the maximum sum of - reward2[i] + reward1[i].

# --------------------------Simpler small----------------------------------
        # base = sum(reward2)
        # diffs = [a - b for a, b in zip(reward1, reward2)]
        # diffs.sort()                      # ascending
        # return base + sum(diffs[-k:])     # last k elements

#---Can use heap too istead of sort--------------------------------------------
# Sort approach: O(n log n) time (because you sort all n diffs).
# Min-heap size k: O(n log k) time (each element does at most one heap op).

#Why greedy???
# DP is for when choices interact across steps.
# Here every cheese contributes an independent “upgrade value” 
# , so the only rational move is: take the best k upgrades.