class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Apparently This is not the solution that your interviewer will be 
        #looking for in an actual interview.
        
        nums1[m:] = nums2[:n] # cool line lol
        nums1.sort()
        
        # nums1 = nums1[:m]       -- lc doesnt accept , dunno y
        # nums1 = nums1 + nums2
        # nums1.sort()
        # print(nums1)

        
        