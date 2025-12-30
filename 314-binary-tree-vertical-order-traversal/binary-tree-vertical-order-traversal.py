# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List
    [int]]:
        if not root: #edgecase
            return []
        q = deque([(root,0)]) #(node,column) 
        columns = {} #{colnumber:arrayofnodes}
        numberofcolumns = 0
        result = []
        while q:
            size = len(q)
            for i in range(size):
                node, col = q.popleft()

                if col not in columns:
                    columns[col] = []
                    numberofcolumns+=1
                columns[col].append(node.val)
                
                if node.left:
                    q.append((node.left, col-1))
                if node.right:
                    q.append((node.right, col+1))

        startcol = min(columns.keys())
        for  i in range(startcol, startcol +  numberofcolumns):
            col = columns[i]
            result.append(col)
        return result

# HINTS
# Do BFS from the root. Let the root be at column 0. In the BFS, keep in the queue the node and its column.

# When you traverse a node, store its value in the column index. For example, the root's value should be stored at index 0.
# If the node has a left node, it column should be col - 1. Similarly, if the node has a right node, its column should be col + 1.

# At the end, check the minimum and maximum col and output their values.