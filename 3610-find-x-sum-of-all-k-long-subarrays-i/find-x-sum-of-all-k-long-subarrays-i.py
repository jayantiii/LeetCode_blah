class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        answer = []
        freq = {}
        maxheap = [] #(-count,-number)
        l,r = 0,0
        #sliding window
        while r < n:
            number = nums[r]
            freq[number] = freq.get(number,0) + 1

            if r-l+ 1 == k: #window complete, make heap
                for num,count in freq.items():
                    heapq.heappush(maxheap,(-1*count,-1*num))
                
                ans = 0
                for _ in range(x): #pop x times from heap
                    if not maxheap:
                        break
                    count, num = heapq.heappop(maxheap) #negative values
                    ans = ans + (count* num)

                answer.append(ans)

                #once done , shift window
                leftele = nums[l]
                freq[leftele] -=1 #reduce one count
                maxheap.clear() # clear heap

                if freq[leftele] == 0:
                    freq.pop(leftele)
                l+=1
            r+=1

        return answer



                
            





#Number of subarrays of size k
# --> n - k + 1 
# Push ( -count, -value ) for each distinct number into a heap (so highest count, then highest value comes first).
#  In Python, a heap compares tuples lexicographically:
# First compares c
# If c ties, then compares v
# If that ties, then next fields, etc.
# So a min-heap of (c, v) uses both: it uses v only when c is equal.
# ---------------
# Summary of what you need to do,
# For each subarray of length k:
# ->Count frequencies.
# ->Pick top x elements by frequency (and by value if tied).
# ->Keep their occurrences and sum them up.
# Return all these sums in a list.

#Window size check: if r - l == k is off by one. A k-length window happens when r - l + 1 == k.

# heapq has no efficient decrease/increase-key or delete arbitrary element, which you’d need when the window slides (counts go up/down). So “carry forward” like freq isn’t directly supported.
# Carry a heap with lazy updates (more complex)
# Every time a count changes, you push a new tuple ( -new_count, -value ).
# When popping, you skip stale entries by checking against the current freq[value].
# This still requires a heap rebuild-ish behavior over time (heap grows), and it’s easy to bug.
