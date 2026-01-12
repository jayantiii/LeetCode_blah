class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #problem forces order: must ship packages in the given sequence.
        def ispossible(shipcap):
            numdays = 1 # start at 1 not zero
            currship = 0
            for i in range(len(weights)):
                if currship + weights[i] <= shipcap: #same ship
                    currship += weights[i]

                else: #newday, newship
                    numdays+=1
                    currship = weights[i]

                if numdays > days:
                    return False

            return True
     
            
        l,r = max(weights), sum(weights) #range max->sum

        while l<=r:
            mid = (l+r)//2
            if ispossible(mid):
                r = mid-1
            else:
                l = mid+1

        return l

# Intuition- Binary seach answer:
# - Capacity C answers a yes/no question: "Can I ship all packages within <= days if the ship holds at most C per day?"
# - If I can do it with C, I can also do it with any larger capacity (monotonic True/False).
# - So: binary search the smallest C that works.


#----------------------Backtracking(not nice way)--------------------------

#         # Backtracking idea:
#         # - "days" means we place (days-1) cut points between packages.
#         # - Each day is a contiguous chunk (order fixed).
#         # - Objective: minimize max(chunk_sum).

#         n = len(weights)
#         prefix = [0]
#         for w in weights:
#             prefix.append(prefix[-1] + w)

#         def segsum(l: int, r: int) -> int:  # sum weights[l:r]
#             return prefix[r] - prefix[l]

#         best = sum(weights)  # upper bound

#         def dfs(day: int, i: int, curr_max: int) -> None:
#             nonlocal best

#             # prune: already worse than best
#             if curr_max >= best:
#                 return

#             # last day must take the rest
#             if day == days:
#                 last = segsum(i, n)
#                 best = min(best, max(curr_max, last))
#                 return

#             # must leave at least 1 package per remaining day
#             # so today's end j can go at most to n - (days - day)
#             max_end = n - (days - day)

#             # try all possible cut positions j (exclusive end for today's chunk)
#             for j in range(i + 1, max_end + 1):
#                 load = segsum(i, j)
#                 new_max = max(curr_max, load)

#                 # prune: extending j only increases load, so if already bad, stop
#                 if new_max >= best:
#                     break

#                 dfs(day + 1, j, new_max)

#         dfs(1, 0, 0)
#         return best

        