class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #Think about XOR
        # XOR all numbers, duplicates cancel out

        res = 0
        for n in nums:
            res = res ^ n
        return res


# can use hashset, add then remove in last only one left
#but hashset soln will use space
# seen = set()
#         for num in nums:
#             if num in seen:
#                 seen.remove(num)
#             else:
#                 seen.add(num)
#         return list(seen)[0]