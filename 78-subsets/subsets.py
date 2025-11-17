class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    #Backtracking, u can make a choice include or not include
    #The number of the subsets is equal ot 2^N, Final time complexity: O(n · 2ⁿ)
    # here n is max possible length of a subset, Space - O(n) - rec stack

        res = []
        def backtrack(index,curr):
            #constraint - every leaf node is a subset
            if index == len(nums): #reached the leaf node for that path
                res.append(curr.copy()) # append a copy, cause list in python is by reference
                return

            #Decision 1 - include
            curr.append(nums[index])
            backtrack(index+1,curr) 
            curr.pop() # It always removes the last element of the list.
            #remove and go to second choice

            #Decision 2 - not include
            backtrack(index+1,curr)

        backtrack(0,[])
        return res

# Brute force?
# outer = [[]]
#         for num in nums:
#             n = len(outer)
#             for i in range(n):
#                 internal = outer[i] + [num]
#                 outer.append(internal)
#         return outer

#For example: nums = [1,2,3]
# Take nums = [1, 2, 3]:
# Start: outer = [[]]
# Process 1:
# current outer: [[]]
# new subsets: [] + [1] = [1]
# outer → [[], [1]]
# Process 2:
# current outer: [[], [1]]
# new subsets: [] + [2] = [2], [1] + [2] = [1, 2]
# outer → [[], [1], [2], [1, 2]]
# Process 3:
# current outer: [[], [1], [2], [1, 2]]
# new subsets: [3], [1, 3], [2, 3], [1, 2, 3]
# outer → [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
# It’s effectively:for each new number, clone all existing subsets and add the number to each clone.

        