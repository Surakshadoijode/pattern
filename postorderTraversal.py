class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
root=TreeNode(11)
obj2=TreeNode(7)
obj3=TreeNode(15)
obj4=TreeNode(5)
obj5=TreeNode(9)
obj6=TreeNode(13)
obj7=TreeNode(20)
obj8=TreeNode(3)
obj9=TreeNode(8)
obj10=TreeNode(10)
obj11=TreeNode(12)
obj12=TreeNode(14)
obj13=TreeNode(18)
obj14=TreeNode(25)

root.left=obj2
root.right=obj3

obj2.left=obj4
obj2.right=obj5

obj3.left=obj6
obj3.right=obj7

obj4.left=obj8

obj5.left=obj9
obj5.right=obj10

obj6.left=obj11
obj6.right=obj12

obj7.left=obj13
obj7.right=obj14

def printPostorder(root):
    if root==None:
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.data,end=" ")
printPostorder(root)
