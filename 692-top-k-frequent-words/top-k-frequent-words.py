class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #My heap apporach, O(n+ulogu+klogu)
        freq = {}
        maxheap = [] #(count,"word")
        res = []
        for i in range(len(words)):
            word = words[i]
            freq[word] = freq.get(word,0) +1

        for u,v in freq.items():
            heapq.heappush(maxheap, (-v,u))

        #pop k times
        while maxheap and k >0:
            c, ele = heapq.heappop(maxheap)
            res.append(ele)
            k-=1

        return res
        

        


#Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
#BUCKET SORTING!!



# Brute Force Intuition
# As we need the most frequent k words, to find which words are of higher frequencies, we just need to sort all words by their frequencies and return the first k words. Notice that the sorting order is first by frequencies and then lexicographically.

#-----------------Simple clean heap-----------------------------
        # cnt = Counter(words)

        # heap = [(-c, w) for w, c in cnt.items()]  # max-heap via negative counts
        # heapq.heapify(heap)

        # return [heapq.heappop(heap)[1] for _ in range(k)]
