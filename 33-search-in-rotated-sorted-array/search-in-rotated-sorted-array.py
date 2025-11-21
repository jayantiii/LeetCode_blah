class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Modified Bineary search

        l,r = 0, len(nums) -1
        while l<=r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if  nums[l] <= nums[mid]: # left sorted portion of array
                if nums[mid] < target or target < nums[l]: #Imp 
                    l = mid +1
                else:
                    r = mid-1
            else : #right sorted portion #nums[mid] <= nums[l]
                if nums[mid] >target or target > nums[r]: ##Imp condn
                    r = mid -1
                else:
                    l = mid+1
                
            # else: # no need here, we need to check target above
            #     return mid

        return -1
        