class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: #this is important
            return -1

        q = deque()
        q.append(("0000",0)) #(state,turns)
        visit = set()
        visit.add("0000") #same as visit = {"0000"}
        dead = set(deadends)

        def nextcombinations(lock,turns): #each digit can go up or down
            res = []
            for i in range(4):
                digit = int(lock[i])
                digitup = (digit +1)% 10  # cause we want 9 to turn to 0
                turnup = lock[:i] +  str(digitup)  + lock[i+1:]

                digitdown = (digit - 1 )% 10   # we want 0 to turn to 9 [ cause -1%10 is = 9]
                turndown = lock[:i] + str(digitdown) + lock[i+1:]

                if turnup not in deadends and  turnup not in visit:
                    res.append((turnup, turns+1))
                    visit.add(turnup)

                if turndown not in deadends and turndown not in visit:
                    res.append((turndown,turns+1))
                    visit.add(turndown)
            return res

        while q :
            lock, turns = q.popleft()
            if lock == target:
                return turns          
            children = nextcombinations(lock,turns)
            for child in children:
                q.append(child)
        return -1 

#BFS!
#one idea can be to initliase visitset with deadends itself

# BFS view:
# - Node = 4-digit lock state (0000..9999) => at most 10^4 nodes total
# - Edge = turn 1 wheel up/down (wrap) => each node has <= 8 neighbors
# - BFS tree = layers by distance (turns); first time we reach target = min turns

# -------------Time / Space:-------------
# Let N = states actually visited (N <= 10^4)
# - Using dead = set(deadends): membership is O(1)
#   Time  = O(N * 8) = O(N)
#   Space = O(N) for visited + queue
# - If deadends stayed a list: membership is O(D)
#   Time  = O(N * 8 * D) = O(ND) (can TLE)

# Worst case: N can be as large as 10⁴ = 10000, because there are only 10,000 possible 4-digit states from "0000" to "9999".


#---------------- Why convert deadends LIST -> SET? -------------------------
# - In Python, `x in some_list` is O(D) because it scans the list linearly
#   (D = len(deadends)).
# - BFS can visit up to N states (N <= 10^4). Each state generates 8 neighbors.
#   So we do ~ (8 * N) membership checks against deadends.
# - If deadends is a LIST:
#       total time ~ (8 * N) * O(D) = O(N * D)   (can be huge / TLE)
# - If deadends is a SET:
#       `x in some_set` is O(1) average (hash lookup),
#       total time ~ (8 * N) * O(1) = O(N)       (fast)
# - Building the set itself costs O(D) once, which is cheap compared to O(N*D).

