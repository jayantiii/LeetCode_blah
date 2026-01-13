class Solution:
    def queryString(self, s: str, n: int) -> bool:
        # O(n * len(s))
        
        for i in range(1,n+1): #loop till n!!
            binary = bin(i)[2:] # Convert i to binary → O(log i)
            
            if binary not in s: # substring search, roughly O(len(s) * len(binary)),
                return False
            
        return True
                  
        
#Small clue:
# Instead of generating all possible substrings of s, it’s more efficient to loop through numbers 1 to n, convert each to binary using bin(i)[2:], and check if it’s in the string s.

#bin(i) in Python returns a string with a prefix that indicates “this is binary”.
# bin(5) → "0b101"
# The "0b" is just a marker, not part of the binary digits.

#-----------------------Optimal ----------------------------
# Key trick: n ≤ 1e9 ⇒ bit_length(n) ≤ 30, so each start position in s generates at most ~30 candidate numbers.

# Optimal approach (O(L · log n))

# Let L = len(s), B = n.bit_length().
# For each start index i:
# Skip if s[i] == '0' (no leading zeros for positive integers).
# Build val incrementally for lengths 1..B:
# val = (val << 1) + current_bit
# Stop early if val > n
# Mark val as “seen”
# At the end, ensure all 1..n are seen.

# seen = [False] * (n + 1)
#         found = 0

#         for i in range(L):
#             if s[i] == '0':
#                 continue  # leading zeros not allowed

#             val = 0
#             for j in range(i, min(L, i + B)):
#                 val = (val << 1) | (s[j] == '1')  # bool acts like 0/1
#                 if val > n:
#                     break
#                 if not seen[val]:
#                     seen[val] = True
#                     found += 1
#                     if found == n:  # early exit: we found all 1..n
#                         return True

#         return False


 #------ naive: build a set of ALL substrings, then query -------------
#         subs = set()
#         L = len(s)

#         for i in range(L):
#             for j in range(i + 1, L + 1):
#                 subs.add(s[i:j])  # slicing copies -> expensive but "naive"

#         for x in range(1, n + 1):
#             if bin(x)[2:] not in subs:
#                 return False
#         return True