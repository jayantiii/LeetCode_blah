class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # O(n2logn)
        n = len(nums)
        answer = []
        freq = {}
        maxheap = [] #(-count,-number) #push -ve of both
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


#Number of subarrays of size k # --> n - k + 1 
# Push ( -count, -value ) for each distinct number into a heap (so highest count, then highest value comes first).
#  In Python, a heap compares tuples lexicographically:
# First compares c
# If c ties, then compares v
# If that ties, then next fields, etc.
# So a min-heap of (c, v) uses both: it uses v only when c is equal.
# ------------------------------------------------------------------
# Summary of what you need to do,
# For each subarray of length k:
# ->Count frequencies.
# ->Pick top x elements by frequency (and by value if tied).
# ->Keep their occurrences and sum them up.
# Return all these sums in a list.

##-----------------------My mistakes------------------------------
#Window size check: if r - l == k is off by one. A k-length window happens when r - l + 1 == k.

# heapq has no efficient decrease/increase-key or delete arbitrary element, which you’d need when the window slides (counts go up/down). So “carry forward” like freq isn’t directly supported.
#Shady Workaaround if needed----
# Carry a heap with lazy updates (more complex)
# Every time a count changes, you push a new tuple ( -new_count, -value ).
# When popping, you skip stale entries by checking against the current freq[value].
# This still requires a heap rebuild-ish behavior over time (heap grows), and it’s easy to bug.

##-----------Non min heap apporach, O(n2logn)------------------------------------------
# I slide a window of size k across the array.
# I keep a frequency map for the current window.
# Add the new right element.
# Remove the left element when the window moves.
# For the current window, I collect all (value, freq) pairs, sort them by:
# higher frequency first, and if tied,higher value first.
# I take the first x pairs from that sorted list and add value * freq to the answer.
# I repeat this for every window.

    # def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    #     n = len(nums)
    #     freq = defaultdict(int)

    #     for i in range(k):
    #         freq[nums[i]] += 1

    #     def compute_x_sum(freq, x):
    #         items = [(v, f) for v, f in freq.items()]
    #         items.sort(key=lambda t: (-t[1], -t[0]))
    #         total = 0
    #         for i in range(min(x, len(items))):
    #             v, f = items[i]
    #             total += v * f
    #         return total

    #     ans = [compute_x_sum(freq, x)]

    #     for i in range(k, n):
    #         add = nums[i]
    #         rem = nums[i - k]
    #         freq[add] += 1
    #         freq[rem] -= 1
    #         if freq[rem] == 0:
    #             del freq[rem]
    #         ans.append(compute_x_sum(freq, x))

    #     return ans
