class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        #backtracking
        res = []
        def backtrack(i,comb,currsum):
            if len(comb)==k: #dont do i==k
                if currsum == n:
                    res.append(comb.copy())
                    return

            if currsum > n:
              return

            for j in range(i,10): #start from i so no duplicate branches:
                backtrack(j+1,comb + [j], currsum+j)
        backtrack(1,[],0)
        return res
    

#if using for loop on j and then dont do 2 choices thing!! (take / not take). IMPPPPPPP!!
#That’s mixing two different recursion patterns in a broken way.

# [0.... 9] root will have 9 branches and  height of tree will be k

#Even though each node can branch to many children (not binary), the maximum number of subsets you can form from 9 elements is still 2⁹.
# Time Complexity (tight bound):
#   Θ(C(9, k) * k)
#   - There are C(9, k) possible k-sized combinations from numbers 1..9. #   - Each valid combination costs O(k) to build/copy into the result.
#2⁹is the upper bound time!
# Space Complexity (auxiliary):
#   O(k)
#   - Recursion depth <= k
#   - Path length <= k

#k = 3, #n = 7
#backtrack(1, [], 0)
# backtrack(2, [1], 1)
# backtrack(3, [1, 2], 3)
# backtrack(4, [1, 2, 3], 6)
# backtrack(5, [1, 2, 4], 7)
# backtrack(6, [1, 2, 5], 8)
# backtrack(7, [1, 2, 6], 9)
# backtrack(8, [1, 2, 7], 10)
# backtrack(9, [1, 2, 8], 11)
# backtrack(10, [1, 2, 9], 12)

# backtrack(4, [1, 3], 4)
# backtrack(5, [1, 3, 4], 8)
# backtrack(6, [1, 3, 5], 9)
# backtrack(7, [1, 3, 6], 10)
# backtrack(8, [1, 3, 7], 11)
# backtrack(9, [1, 3, 8], 12)
# backtrack(10, [1, 3, 9], 13)

# backtrack(5, [1, 4], 5)
# backtrack(6, [1, 4, 5], 10)
# backtrack(7, [1, 4, 6], 11)
# backtrack(8, [1, 4, 7], 12)
# backtrack(9, [1, 4, 8], 13)
# backtrack(10, [1, 4, 9], 14)
# ..... more and more