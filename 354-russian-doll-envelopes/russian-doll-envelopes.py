class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#sort (w asc, h desc) to avoid equal-width being counted in LIS
        envelopes.sort(key= lambda x:(x[0],-x[1]))
#tails[L-1] = smallest possible ending height among all valid chains of length L.

        tails = []
        for i in range(len(envelopes)):
            w1,h1 = envelopes[i][0], envelopes[i][1]

            ## find the insertion point in the Sort order:
            idx = bisect_left(tails,h1) #Bineary search

            if idx == len(tails): #length increase
                tails.append(h1)
            else:
                tails[idx] = h1
            
        return len(tails)

# O(n log n) LIS version
# You don’t store dp[i] for each envelope. Instead you store DP by length:
# tails[i] = smallest possible ending height of an sequence of length i+1.

#Think of it as keeping your options open for future, smaller heights.

# Instead of checking every envelope against every other envelope (O(N^2)),
# we use binary search to find where the current height fits in our "best-so-far" list (O(N log N)).

# If the new height is larger than anything in tails, it extends our longest chain.
# If the new height is smaller, it replaces an existing value. This doesn't change the length of our current chain,

# So for each length L, we keep the smallest possible ending height because it gives the most future options. Keeping the largest ending height would throw away extendable possibilities and can block building longer chains later.

#EXAMPLE!!
# envelopes: [[5,4],[6,4],[6,7],[2,3]]
#
# Sort (w asc, h desc) -> [[2,3],[5,4],[6,7],[6,4]]
# Heights -> [3,4,7,4]

# tails = "best endings":
#tails[i] = smallest ending height for a chain of length i+1
#
# h=3  -> tails=[3]        # made length 1
# h=4  -> tails=[3,4]      # made length 2
# h=7  -> tails=[3,4,7]    # made length 3
# h=4  -> idx=1, replace tails[1]=4 (no change)  # length stays 3
#
# Answer = len(tails) = 3

#--------------DP LIS, SEE! ---------------------------------------------------     
#dp[i] = the maximum number of envelopes you can nest if you MUST end with envelope i as the outermost (last) one.

        #if same width, diff height then cant so we tie break such
        #that if same width, height is sorted in decreasing order

        # envelopes.sort(key= lambda x:(x[0],-x[1]))
        # dp = [1 for i in range(len(envelopes))]

        # for i in range(len(envelopes)):
        #     w1,h1 = envelopes[i][0], envelopes[i][1]
        #     for j in range(i):
        #         w2,h2 = envelopes[j][0], envelopes[j][1]
        #         if w1> w2 and h1>h2: #needed
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)

#------------Why we sort like that?-----------------------------------------------
# Sorting by width helps, but it does not make the problem “monotone” enough for a 2-pointer scan. The key is: sorting is just an ordering, it doesn’t magically make every earlier envelope “fit” into every later envelope.

# If you do two nested loops over all envelopes just once, still not guaranteed correct (without sorting), because you’ll sometimes use a dp[j] that hasn’t reached its final value yet.

# Two pointers works when “if I advance one pointer, I never regret it” (classic: merging sorted lists, interval intersections, sliding window with a monotone constraint).

# Russian-doll is a subsequence optimization: you often must skip a currently valid choice to get a longer chain later. That breaks the “never regret” property.

# ✅ DP O(n²): width-only sort is fine (as long as you still check wj < wi and hj < hi)
# ❌ LIS O(n log n): width-only sort is not fine; you must sort (w↑, h↓) to avoid the equal-width bug

#----------example to understand-------------------------------------------
#ONE MORE EXAMPLE FOR FIRST ANSWER

# If Heights were [3, 4, 7, 5] instead:

# tails meaning: tails[i] = smallest possible ending height of a chain of length (i+1)

# h=3:
#   tails = [3]          # best length-1 chain ends at 3

# h=4:
#   tails = [3, 4]       # best length-2 chain ends at 4

# h=7:
#   tails = [3, 4, 7]    # best length-3 chain ends at 7

# h=5:
#   idx = bisect_left([3,4,7], 5) = 2
#   replace tails[2] = 5 -> tails = [3, 4, 5]
#   IMPORTANT: length stays 3 (still have a length-3 chain),
#   but now it ends at 5 instead of 7, which is "cheaper" and easier to extend later with any height > 5.

# Answer is still len(tails) = 3
# (and if a later height like 6 appears, [3,4,5] can extend to length 4, but [3,4,7] could NOT)

        