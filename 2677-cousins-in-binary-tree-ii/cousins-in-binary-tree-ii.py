# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []  #level sums, 0..1...2

        #level order - BFS
        q = deque([root])
        levelsum = 0
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                levelsum += node.val
                if node.left:   
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(levelsum)
            levelsum = 0 #reset, donr forget

        #update the value of the node with the sum of the values of the current level - sibling node’s values.
        def dfs(node,level):
            if not node:
                return
    
            # sibling sum for the next level = sum of this parent's children (original values)
            leftchild = node.left.val if node.left else 0
            rightchild= node.right.val if node.right else 0
            sib_sum = leftchild + rightchild #(exclude both so sib_sum)

            if node.left:
                node.left.val = res[level+1] - sib_sum 

            if node.right:
                node.right.val = res[level+1] - sib_sum 
       
            dfs(node.left, level+1)
            dfs(node.right,level+1)
              
        
        root.val = 0 #this
        dfs(root, 0) # #Also root, root.left and root.right will be zero
        return root

#1)For the first step, find the sum of values of all the levels of the binary tree.
#2)For the second step, update the value of the node with the sum of the values of the current level - sibling node’s values. 
#Both step O(n)

#logic on how to find siblings, we dont need to find it though, just find the sum!
# “sibling” logic: siblings are just the two children of the same parent, so compute sibling-sum at the parent and update both children.

##------------------ Do step 1 using DFS-----------------------------------------
# def dfs_sum(node, lvl):
#     if not node: 
#         return
#     if lvl == len(level_sums):
#         level_sums.append(0)
#     level_sums[lvl] += node.val
#     dfs_sum(node.left, lvl+1)
#     dfs_sum(node.right, lvl+1)

#------------------------- Do step 2 using BFS------------------------------------
       # # 2) update using parent context (parent knows both siblings)
        # root.val = 0
        # q = deque([(root, 0)])  # (node, level)
        # while q:
        #     node, lvl = q.popleft()
        #     next_lvl = lvl + 1
        #     if next_lvl >= len(level_sum):
        #         continue

        #     sib_sum = 0
        #     if node.left: sib_sum += node.left.val
        #     if node.right: sib_sum += node.right.val

        #     if node.left:
        #         node.left.val = level_sum[next_lvl] - sib_sum
        #         q.append((node.left, next_lvl))
        #     if node.right:
        #         node.right.val = level_sum[next_lvl] - sib_sum
        #         q.append((node.right, next_lvl))

        # return root

# ---------Modify DFS to update node.val inside its own call, not so good--------------------
# def dfs(node, level, sib_group_sum):
#     if not node:
#         return

#     # update THIS node
#     if level == 0:
#         node.val = 0
#     else:
#         node.val = levelSum[level] - sib_group_sum

#     # compute sibling-group sum for children BEFORE recursing (children still have original vals)
#     child_group_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)

#     dfs(node.left, level + 1, child_group_sum)
#     dfs(node.right, level + 1, child_group_sum)

# # call:
# dfs(root, 0, root.val)  # sib_group_sum unused for root anyway