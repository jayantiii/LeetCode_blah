class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #nums1 is subset of nums2
        #give answer only if it present innums1, meaning len(output) == len(nums1)
        output = [-1] * len(nums1) #necessary
        stack = []
        nums1map = {} #look up in hash is 0(1)
        for i in range(len(nums1)):
            nums1map[nums1[i]] = i

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]: # run for all ele
                ele = stack.pop()
                if ele in nums1: #check here not before while
                    index = nums1map[ele]
                    output[index] = nums2[i]
            stack.append(nums2[i]) # push every ele from nums2 in stack 
        return output

#Note - The current nums2[i] can be the next greater element for some previous value that is in nums1, even if nums2[i] itself is not in nums1.
#If no next greater element exists, the answer must be -1.

        