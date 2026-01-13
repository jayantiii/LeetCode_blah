class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

# it says input size is 10 to power 5, means we need O(n) answer

#Idea use sliding window of length 10 and hashmap to track substr frequencies

        l, r = 0, 10  #not 9
        substr_map = {}
        res = []

        while r <= len(s):
            # Wrong!!  - if s[l:r] in substr_map and not "Done":
            if s[l:r] in substr_map and substr_map[s[l:r]] != "Done":
                res.append(s[l:r])
                substr_map[s[l:r]] = "Done"
            else:
                if s[l:r] not in substr_map: # using if so that "Done" not rewritten
                    substr_map[s[l:r]] = 1 # only this in else fails, can rewrite "Done"

            l +=1
            r+=1
        return res


#this is apparently correct better approach

# while r <= len(s):
#     substr = s[l:r]
#     substr_map[substr] = substr_map.get(substr, 0) + 1
#     if substr_map[substr] == 2:  # Add only when count becomes 2
#         res.append(substr)
#     l += 1
#     r += 1




        