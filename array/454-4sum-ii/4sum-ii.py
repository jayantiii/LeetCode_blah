class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        n = len(nums1)
        hashset = {}
        for i in range(n): #nums3
            for j in range(n): #nums4
                added = nums3[i] + nums4[j]
                hashset[added] = hashset.get(added,0) + 1

        for i in range(n): #nums1
            for j in range(n): #nums2
                need = (nums1[i] + nums2[j])*-1
                if need in hashset:
                    count += hashset[need]   # <-- add frequency, not 1
      
        return count
        


        
#Brute -> N^4 (easy one)
# Optimised -> N^3 (just create a hash map for last array)
# Further Optimised -> N^2 (create a hash map for last two arrays)
# hint -> mpp[ nums3[i] + nums4[j] ]++;

# you add the frequency because each occurrence corresponds to a different pair of indices, and the problem counts quadruples of indices, not “unique value sets.”