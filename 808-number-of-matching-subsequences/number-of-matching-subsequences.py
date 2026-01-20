import bisect
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hashmap = defaultdict(list)
        #hashmap of all chars and their indices they present it
        for i in range(len(s)):
            letter = s[i]
            hashmap[letter].append(i)

        def bnysearch(word):
            previ = -1 #last macthed index in 
            for i in range(len(word)):
                char = word[i]
                idxs = hashmap.get(char,[])
                j = bisect.bisect_right(idxs,previ) #first index index > prev

                if j ==len(idxs):return False #not found
                previ = idxs[j]
            return True
                
        count = 0
        for word in words:
            if bnysearch(word):
                count+=1

        return count
        

#If getting TLE just try reducing your words size by mapping each word with its frequency, and using that maps unique words to check for subsequence instead of actual words arrays.

# HashMap + Binary Search
# HashMap for storing main string's character index
# Binary Search for checking each individual word can be created using above hashmap or not


# #--------Brute force--------------------------------------
# Brute force = for each word, walk through s with two pointers.
#         def is_subseq(w: str) -> bool:
#             i = 0  # pointer in w
#             for ch in s:              # scan s fully
#                 if i < len(w) and w[i] == ch:
#                     i += 1
#                     if i == len(w):
#                         return True
#             return i == len(w)

#         count = 0
#         for w in words:
#             if is_subseq(w):
#                 count += 1
#         return count
 
