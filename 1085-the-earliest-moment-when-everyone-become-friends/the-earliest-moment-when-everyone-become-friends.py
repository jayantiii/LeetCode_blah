class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        #Hint - sort log items by timestamp, so we know who became friends earliest
        #then visisualise the problem, its like merging (union find)
        logs.sort(key = lambda x:x[0])
        friends = {i:set() for i in range(n)}
        for t, u, v in logs:
            groupu =  friends[u]
            groupv =  friends[v]

            # skip only if they already point to the SAME set object
            if groupu is groupv and groupu:
                # if they share a non-empty group, nothing to do
                continue

            merged = groupu.union(groupv)
            merged.add(u) # needed cause first loop, merged will be union of 2 empty sets
            merged.add(v)

            # # point everyone in merged group to the same set
            for f in merged:
                friends[f] = merged
            if len(merged) == n: #merged includes all urself
                return t
        return -1


        


           
            



#This below exmaple is hint on union find
# The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
# The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].

#So we are connecting p1 and p2 that would mean whoever is conencted to p1 is also connected to P2 and vice versa

# Idea:

# Sort logs by time.

# Start with n separate components.

# For each log [t, a, b] (in time order), union a and b.

# Each successful union reduces the number of components.

# When the number of components becomes 1, return that time t.

# If it never becomes 1, return -1.