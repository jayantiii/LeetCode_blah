class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        result = [root.val]
        for child in root.children:
            result.extend(self.preorder(child))
        return result

#see how to do!!