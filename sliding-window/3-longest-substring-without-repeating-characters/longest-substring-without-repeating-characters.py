class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#use sliding window - l and r
        char_map = {}  # Tracks most recent index of each char!!!
        max_len = 0
        l = 0
        for r in range(len(s)):
            letter = s[r]
# and is imp,  Update left pointer ONLY if duplicate is IN CURRENT WINDOW
            if letter in char_map and char_map[letter] >=  l: 
                l = char_map[letter] +1

            #update latest index
            char_map[letter] = r
            max_len = max(max_len, r-l+1) ## not l--r

        return max_len
            





# For example, with string "abcabcbb":

# Start with window "a", then expand to "ab", then "abc"
# When we hit the second 'a', we have "abca" which is invalid
# Instead of restarting, we shrink from left: remove first 'a' to get "bca"
    

        