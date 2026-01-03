class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead= set()
        self.inheritance = {kingName:[]} #parent:child
        

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)
        self.inheritance[childName] = [] #no child yet

    
    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]: # there is no left anf right pointers ok!
        order = []
        def preorder(node): #root,left, right
            if not node:return
            if node not in self.dead:
                order.append(node)
              
            for child in self.inheritance[node]:
                preorder(child)

        preorder(self.king)

        return order

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()


#just a fancy way to say pre-order traversal of a tree.
#Order -> King -> Olderchild ->olderchildschild ->nextkingschild
#This problem is literally a rooted family tree where the inheritance order is preorder DFS (visit node, then children in birth order), skipping dead names. A hashmap/dict parent -> [children...] is perfect because births must preserve insertion order.

##-----Iterative pre-order traversal--------------------------------------
    # def getInheritanceOrder(self) -> List[str]:
    #     # Iterative preorder traversal to avoid recursion depth issues
    #     order: List[str] = []
    #     stack = [self.king]

    #     while stack:
    #         person = stack.pop()

    #         # Visit (preorder): record if alive
    #         if person not in self.dead:
    #             order.append(person)

    #         # Push children in reverse so oldest is processed first
    #         kids = self.children.get(person, [])
    #         for child in reversed(kids):
    #             stack.append(child)

    #     return order