class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # graph = { char: set(neighbors) }
        # indegree = { char: number_of_incoming_edges }
         # 1) Collect all unique characters
        letters = {} #store sets cause we dont want letters to repeat
        indegree = {} #indegree cant be array cause no correlation between index and chars
        for word in words:
            for char in word:
                if char not in letters:
                    letters[char] = set()
                    indegree[char] = 0 # initialize so nodes with no incoming edges get an indegree entry.

         # 2) Build graph by comparing adjacent words
        for i in range(1,len(words)):
            w1, w2 = words[i - 1], words[i]
            j = 0
            min_len = min(len(w1), len(w2))

            # Find first differing character, index j
            while j < min_len and w1[j] == w2[j]: #compare chars not words
                j+=1

            # Case A: all chars same up to min_len
            if j == min_len:
                # Invalid: ["abc", "ab"] -> no valid order
                if len(w1) > len(w2):
                    return ""
                # Otherwise, no new constraint from this pair
                continue

            # Case B: w1[j] != w2[j], we have ordering: w1[j] -> w2[j]
            prevchar = w1[j]
            currchar = w2[j]
            
            # Only add edge and indegree once
            if currchar not in letters[prevchar]:
                letters[prevchar].add(currchar)
                indegree[currchar] += 1

        # 3) Use indegree to see where to start building topological sort graph from
        start = [key for key, val in indegree.items() if val == 0]
        order = []
        q = deque(start)
        while q:
            char = q.popleft()
            order.append(char)
            for nei in letters[char]:
                indegree[nei] -=1
                if indegree[nei] == 0: #this
                    q.append(nei)

        # 4) If cycle: not all chars appear in order -> return ""
        numchars = len(letters)
        if len(order) != numchars:
            return ""

        return "".join(order)

#Questions is find the what does lexicographical order mean in alien world
#IMPORTANT - My mistake
# You cannot infer letter order just by looking inside a single word.
# The ordering info comes from how words compare to each other, not from positions of letters inside one word.

#---------- Topological sort (Kahn’s algorithm)---------
# Once graph + indegree are built:
# Start with a queue of all nodes whose indegree == 0.
# Pop from queue, append to result.
# For each neighbor, decrement indegree; if it becomes 0, push to queue.
# At end:
# If result length == number of unique letters → valid order.
# Else → cycle → return "".

# Mental blueprint for the interview
# Nodes: all unique chars in words.
# Edges: compare each adjacent pair, find first differing char, add from → to.
# Invalid prefix case: if longer word comes before its prefix, return "".
# Topo sort: BFS over indegree-0 nodes → result string.
# If cycle (not all nodes output) → "".
