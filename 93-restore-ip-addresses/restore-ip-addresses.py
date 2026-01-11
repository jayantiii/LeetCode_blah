class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        res = []
        # we have 4 dots, think where to put each

        def backtrack(i,dots, currip):
            # minimal: stop if we already used too many segments
            if dots < 0:
                return

            if dots == 0 and i == len(s) : #both is base case
                res.append(currip) #strings dont have copy
                
            for j in range(i,min(i+3,len(s))):
                value = s[i:j+1] #this!
                if int(value) <= 255:

                #It ensures a segment can be "0" but 
                # cannot have leading zeros like "00" or "01".
                    if i==j or s[i]!="0":

                        backtrack(
                            j + 1,
                            dots - 1,
                            currip + value + ("." if dots > 1 else "")
                        )

        backtrack(0,4,"") #start with empty

        return res

# Level 0 (Start)             [ "" ]
#                              /  |  \
# Level 1 (Seg 1)          "2"   "25"  "255"
#                         / | \   ...    |
# Level 2 (Seg 2)      "5" "55" ...     "2"   "25"  "255"
#                       |    |           |     |      |
# Level 3 (Seg 3)      ...  ...         "5"   "55"   "1"  "11"
#                                        |     |      |    |
# Level 4 (Seg 4)                       ...   "11"   "1" (End of String!)
#                                              ^      ^
#                                            Valid  Invalid (String not empty)

# def leading_0(string):
#     return string[0] == "0" and string != "0"

# def valid(part):
#     return not leading_0(part) and int(part) <= 255

# def valid_ip(nums):
#     return all(valid(part) for part in nums)

# class Solution:
#     def restoreIpAddresses(self, s: str) -> List[str]:
#         ret = []
#         for i, j, k in itertools.combinations(range(1, len(s)), 3):
#             ip = [s[:i], s[i:j], s[j:k], s[k:]]
#             if valid_ip(ip):
#                 ret.append(".".join(ip))
#         return ret

        