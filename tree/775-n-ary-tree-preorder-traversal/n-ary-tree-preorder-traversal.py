class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = [root.val]  # Start with root value
        for child in root.children:
            # Collect ALL children's preorder results
            result.extend(self.preorder(child))
        return result

# Dry run of fixed version:
# preorder(1):
#   result = [1]
#   child = 2: result.extend(preorder(2)) → [1, 2, 5, 6]
#   child = 3: result.extend(preorder(3)) → [1, 2, 5, 6, 3]
#   child = 4: result.extend(preorder(4)) → [1, 2, 5, 6, 3, 4]
#   return [1, 2, 5, 6, 3, 4]