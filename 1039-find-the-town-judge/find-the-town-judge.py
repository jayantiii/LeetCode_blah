class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        outdegree = [0]*(n+1) #1 based indexing
        indegree = [0]*(n+1)
        for u,v in trust:
            outdegree[u] +=1
            indegree[v] +=1

        for i in range(1,n+1):
            if outdegree[i] == 0 and indegree[i] == n-1:
                return i
        return -1

        



# Observations:
# The town judge trusts nobody → their out-degree is 0.
# Everybody else trusts the judge → their in-degree is n - 1.
# So, instead of building a full graph, you just need to track in-degrees and out-degrees for each person.

##-----------------------Similar idea but one array only,-----------------------
#At the end, the townjudge will have score[i] == n-1
        # score = [0] * (n + 1)  # 1-based indexing

        # for a, b in trust:
        #     score[a] -= 1  # trusts someone, cannot be judge
        #     score[b] += 1  # trusted by someone

        # for i in range(1, n + 1):
        #     if score[i] == n - 1:
        #         return i

        # return -1
