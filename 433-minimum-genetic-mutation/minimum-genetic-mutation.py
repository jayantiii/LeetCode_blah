class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        q = deque()
        q.append((startGene,0)) #(gene, mutationstoreach)
        choices = ["A", "C", "G", "T"]
        def nextmutations(gene, mutations):
            child = []
            for i in range(8):
                for ch in choices:
                    if ch == gene[i]:
                        continue
                    newgene = gene[:i] + ch + gene[i+1:] #do like this, since strings immutable
                    if newgene in bank and newgene not in visited:
                        child.append((newgene,mutations+1))
                        visited.add(newgene)
            return child
    
        while q:
            #gene string - 8-character long string
            gene, mutations = q.popleft()
            if gene == endGene:
                return mutations
            children = nextmutations(gene, mutations)
            for child in children:
                newgene, mutation = child
                if newgene == endGene:
                    return mutation
                q.append(child)
        return -1
                
                
            



#You think BFS here because the problem is secretly:
#“Minimum number of single-step moves from start to end in an unweighted graph.”

# Mental mapping → BFS trigger
# State = a gene string (8 chars).
# Edge = one valid mutation (change exactly 1 char AND resulting string is in bank).
# Every edge costs 1 mutation (uniform cost).
# Question asks minimum number of steps.
# That is exactly shortest path in an unweighted graph → BFS.

#-------How many children can a node have (max) in a tree? (visualise) ?---------
# A gene length is 8.so, 8×3=24
# At each position, you can change the current letter to 3 other letters (A/C/G/T minus itself).
# So possible one-step mutations you can generate: ==> 8×3=24
# So the theoretical max branching is 24, not 32.
# But the actual number of children is usually much smaller because:
# only mutations that are in bank are valid nodes and you also exclude visited nodes


# ------------------ Time and Space -------------
# # Time / Space:
# # Let B = len(bank), L = 8, alphabet size = 4.
# # Each gene expansion tries at most L*3 = 24 candidate mutations (constant).
# #
# # If bank is a SET: membership is O(1) average
# #   Time:  O(B * L * 3) = O(B)   (since L=8 is constant)
# #   Space: O(B) for visited + O(B) for queue (+ O(B) for bank_set) => O(B)
# #
# # If bank is a LIST: membership is O(B)
# #   Time:  O(B * (L*3) * B) = O(B^2)
# #   Space: still O(B)
        