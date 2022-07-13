**#Recursive**
def levelOrder(self, root):
if not root:
return []
answer = []
self.traverse(root, 1, answer)
return answer
def traverse(self, node, level, answer):
if not node:
return
if level > len(answer):
# we are at a new level
answer.append([node.val])
else:
answer[level-1].extend([node.val])
self.traverse(node.left, level + 1, answer)
self.traverse(node.right, level + 1, answer)