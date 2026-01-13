class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*(26) #longest subs found so far ending at that char

        for ch in s:
            a,z = ord('a'), ord('z')
            # Check only letters within distance k
            start = ord(ch) - k
            end = ord(ch) + k 

            #make it in 0-25 range and # Use max/min to stay inside the 0-25 range
            # max/min needed cause if char is 'a' ,start can go negative too
            start = max(0,start - a)
            end = min(25,end - a)
            currch = ord(ch) - a
            bestprev = 0
            for i in range(start, end+1): # end +1 needed
                if dp[i] > bestprev:
                    bestprev = dp[i]

            dp[currch] = max(dp[currch],bestprev + 1)

        return max(dp)

# Time  : O(n * min(26, 2k+1))  <= O(26n) = O(n)

#-----------MY mistakes ------------
#1)I tried doing -  dp[i] = dp[i] +1
# - You are incrementing dp[i] for everyone in the neighborhood. This would mean if you see the letter 'c', you are changing the scores for 'a', 'b', 'd', and 'e'. That's not right—only the score for 'c' should change based on who it can "attach" to.

#2)i tried doing --  # dp[currch] = max(dp[currch],dp[i] +1)
#dont do in place like this, wrong. use bestprev like shown and update after loop
# Because you’re updating dp[currch] while you’re still reading from dp, and your read-range includes currch itself (i == currch). That lets the current character “use itself” and artificially grow by 2+ in the same iteration.

#----------- Bruteforce answer loop , works but TLE and MLE------------
#         longestideal = 0
#         res = [""]
#         for ch in s:
#             size = len(res)
#             for i in range(size):
#                 oldsub = res[i]
#                 if oldsub == "" or abs(ord(oldsub[-1]) - ord(ch)) <= k:
#                     longestideal = max(longestideal, len(res[i])+1)
#                     res.append(res[i]+ch)
#         return longestideal

# #Understand, dont think its n2 just cause 2 loops ---->
# Time Complexity: $O(2^n). Each character can either be added to all existing subsequences or not.
# .Space Complexity: $O(2^n. n). You are storing 2^n strings, and each string has an average length n

#---- DFS soln ---------------------------
    # def longestIdealString(self, s: str, k: int) -> int:
    #     n = len(s)
    #     a = ord('a')

    #     @lru_cache(None)
    #     def dfs(i: int, last: int) -> int:
    #         if i == n:
    #             return 0

    #         # Option 1: skip s[i]
    #         best = dfs(i + 1, last)

    #         # Option 2: take s[i] if allowed
    #         cur = ord(s[i]) - a
    #         if last == 26 or abs(cur - last) <= k:
    #             best = max(best, 1 + dfs(i + 1, cur))

    #         return best

    #     return dfs(0, 26)

  # #states = (n+1) * 27  => O(n)
        # Time  : O(27 * n) = O(n)   (each state does O(1) work: skip/take)
        # Space : O(27 * n) = O(n)   (memo table)
        #         + O(n) recursion stack

# ----------------#Brute force way to find all subsequences -------------------
#    def allSubsequences(self, s: str) -> List[str]:
        # res = [""]  # start with empty subsequence

        # for ch in s:
        #     # for every existing subsequence, add a new one with `ch` appended
        #     size = len(res)
        #     for i in range(size):
        #         res.append(res[i] + ch)

        # return res

