class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        totalsum = sum(nums)

        def dfs(arr, turn, s1, s2): #return max score player 1 can get
            # returns the final total score that Player 1 can guarantee
            if not arr:
                return s1 #return score, not 0
            if turn == 1:
                first = dfs(arr[1:],2, s1 + arr[0], s2)
                last = dfs(arr[:-1],2, s1 + arr[-1], s2)
                return max(first,last)

            if turn == 2:
                first = dfs(arr[1:],1, s1, s2 + arr[0])
                last = dfs(arr[:-1],1, s1, s2 + arr[-1])
                return min(first,last) #IMPPP, minimise turn 2 scores
           
            return max1

        max1 = dfs(nums,1,0,0)
        if max1 * 2 >= totalsum: # better than doing totalsum//2
            return True
        else:
            return False








        