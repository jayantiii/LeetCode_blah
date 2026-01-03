from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #Main Point - count freq of chars in s and the loop through order!!
        count = Counter(s)
        finals = ""
        for char in order:
            if char in count:
                finals = finals + char*count[char]
                del count[char]

        #if a char not present in order
        for key,val in count.items():
            finals = finals + key*val
        return finals

 # Why list + join instead of doing `ans += ...`?
        # - Strings are immutable in Python.
        # - Repeated `ans += piece` makes a NEW string each time, copying old content -> O(N^2).
        # - List appends are O(1) amortized, and `"".join(out)` builds the final string once -> O(N).
        
 # pop(ch, 0) is better than `if ch in cnt: del cnt[ch]` because:
            # - it safely returns 0 if ch is missing (no KeyError)
            # - it removes ch from cnt in the same operation




        