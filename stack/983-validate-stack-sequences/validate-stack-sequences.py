class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        x = 0 #pop array pointer
        stack = []
        for push in pushed:
            stack.append(push)
            while stack and (stack[-1] == popped[x]):
                stack.pop()
                x+=1

        if (len(stack) == 0) and (x == len(popped)):
            return True

        return False

# Simulate a real stack:
#  push each value from pushed, and after every push, 
#  pop while the stack top equals the next needed value in popped (tracked by pointer x).

# This is correct because a stack can only pop the top; if the top matches what you must pop next, popping immediately can’t hurt.
# At the end, it’s valid iff you matched all pops (x == len(popped)) and the stack is empty.

# -------Common follow-ups + how to solve ---------------------------
# 1) "Return the push/pop operations (one valid sequence), not just True/False"
#    -> Same simulation; whenever you push record "push x", whenever you pop record "pop".
#    -> If you finish with all pops matched, return ops else impossible.

# 2) "Duplicates allowed in pushed/popped?"
#    -> Value-only compare can match the wrong copy.
#    -> Tag elements by index (treat each push as a unique ID), or use counts+positions if constrained.

# 3) "Many popped queries for the same pushed (Q queries)"
#    -> Run the same O(n) simulation per query (each element pushes/pops once).
#    -> Typical expected answer: O(Q*n), unless extra constraints enable precomputation.

# 4) "Streaming popped (you receive popped one-by-one) — can you validate online?"
#    -> Keep the same stack; push from pushed as needed until top matches next pop or you run out.
#    -> If next pop can't be matched, fail immediately.

# 5) "Queue instead of stack?"
#    -> For a queue, pop order must exactly match push order (popped == pushed) for validity.

# 6) "Deque (pop from either end) instead of stack?"
#    -> Simulate with a deque; for each needed pop, check left end or right end matches and pop it.
#    -> If neither end matches, fail.




        
        