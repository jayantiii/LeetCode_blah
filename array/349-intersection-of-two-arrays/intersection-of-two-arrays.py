class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #it means that elements that are common on both array.
        return list(set(nums1) & set(nums2))