class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heap, Use a min-heap of size k (optimal method), Keep the k largest elements seen so
        #Since its min heap, root will hold the kth element
        minheap = []
        for i in range(len(nums)):
            if len(minheap) < k:
                heapq.heappush(minheap,nums[i])
            else:
                heapq.heappushpop(minheap,nums[i])
        return minheap[0]

#This method is a combination of two operations: heappush() and heappop(). It allows you to push a new element onto the heap and then pop the smallest element in one atomic operation            

#Bruteforce
#- just sort and then return the kth index from last

#oTHER heap , but not nice way to do it
        # heapq.heapify(nums)  # in-place, returns None

        # # Remove the smallest (n - k) elements,
        # # so the root becomes the k-th largest.
        # for _ in range(len(nums) - k):
        #     heapq.heappop(nums)

        # return nums[0]  # now the k-th largest