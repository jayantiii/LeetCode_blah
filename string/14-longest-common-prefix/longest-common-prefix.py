class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #make prefix first word
        prefix = strs[0]
        pre_len = len(prefix)

        for i in range(1,len(strs)):
            while prefix != strs[i][:pre_len]:
                # decrease pre_len and prefix by 1 char
                pre_len -=1
                prefix = prefix[:pre_len]

        return prefix








#One Another way!!
        # # handle empty
        # if not strs:
        #     return ""
        # n = len(strs)
        # # the trick is that this sorts lexicographically
        # # Thus, common prefix of first and last is guaranteed to be the common prefix of every string in the list.
        # strs.sort()
        # first = strs[0]
        # last = strs[-1]
        # i = 0 # only one pointer needed
        # while i < len(first) and first[i] == last [i]:
        #     i+=1
        # return first[:i]
        

        



# Think about:

# What's the maximum possible length of the common prefix?
# How can you efficiently check if all strings share the same character at position i?
# When should you stop checking further characters?

# Simple Starting Point: Take the first string as initial prefix, then compare with each subsequent string, trimming the prefix as needed.