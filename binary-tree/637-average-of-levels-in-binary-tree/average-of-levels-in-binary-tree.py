# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        res = []
        while q:
            size = len(q)
            levelsum = 0
            for _ in range(size):
                node = q.popleft()
                levelsum += node.val

                if node.left: #check first
                    q.append(node.left) #dont forget!

                if node.right:
                    q.append(node.right)

            avg = levelsum/size
            res.append(avg)

        return res

        