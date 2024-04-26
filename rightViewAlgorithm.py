class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

root = Node(11)
obj2 = Node(7)
obj3 = Node(15)
obj4 = Node(5)
obj5 = Node(9)
obj6 = Node(13)
obj7 = Node(20)
obj8 = Node(3)
obj9 = Node(8)
obj10 = Node(10)
obj11 = Node(12)
obj12 = Node(14)
obj13 = Node(18)
obj14 = Node(25)

root.left = obj2
root.right = obj3

obj2.left = obj4
obj2.right = obj5

obj4.left = obj8
obj5.left = obj9
obj5.right = obj10

obj3.left = obj6
obj3.right = obj7

obj6.left = obj11
obj6.right = obj12

obj7.left = obj13
obj7.right = obj14

def rightViewOfBinaryTree(root):
    result = []
    Q = [root]
 
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            # step-1: popping
            curr = Q.pop(0)
            if i == n - 1:
                result.append(curr.data)
 
            # step-2: pushing left child if its not none 
            if curr.left != None:
                Q.append(curr.left)
 
            # step-3: pushing right child if its not none
            if curr.right != None:
                Q.append(curr.right)
    print(*result)
rightViewOfBinaryTree(root)
