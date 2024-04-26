class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def leftboundary(root,result):
    while root!=None:
        if root.left==None and root.right==None:
            break
        result.append(root.data)
        if root.left!=None:
            root=root.left
        else:
            root=root.right    

def leafnodes(root,result):
    if root==None:
        return
    if root.left==None and root.right==None:
        result.append(root.data)
    leafnodes(root.left,result)
    leafnodes(root.right,result)    

def rightboundary(root,result):
    temp=[]
    while root!=None:
        if root.left==None and root.right==None:
            break

        temp.append(root.data)

        if root.right!=None:
            root=root.right
        else:
            root=root.left    
    temp=temp[::-1] 
    for ele in temp:
        result.append(ele)
        
def boundary(root):
    result=[]
    result.append(root.data)
    #collect left boundary
    leftboundary(root.left,result)
    leafnodes(root,result)
    #ritght boundary
    rightboundary(root.right,result)
    print(*result)
root=node(11)
obj2=node(7)
obj3=node(15)
obj4=node(5)
obj5=node(9)
obj6=node(13)
obj7=node(20)
obj8=node(3)
obj9=node(8)
obj10=node(10)
obj11=node(12)
obj12=node(14)
obj13=node(18)
obj14=node(25)

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

boundary(root)
