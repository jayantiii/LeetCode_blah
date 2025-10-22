class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # idea have a window of k size? can do without it, no need of l, r also
        char_map = {} # last index of a element


        for i in range(len(nums)):
            if nums[i] in char_map:
                if abs(i- char_map[nums[i]]) <= k:
                    return True
                else:
                    char_map[nums[i]] = i
            else:
                char_map[nums[i]] = i
        return False

        




# Idea - Use a hash map to track the most recent index of each number. If you find a duplicate, check if the distance between current and previous index ≤ k.