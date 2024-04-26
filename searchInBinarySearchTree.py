class Node:
    def __init__(self,data):
        self.data = data
        self.right =   None
        self.left = None

n=int(input())
num=list(map(int,input().split()))
target=int(input())

def insertIntoBST(root,ele):
    if root==None:
        new=Node(ele)
        return new
    if root.data<ele:
        root.right=insertIntoBST(root.right,ele)
    else:
        root.left=insertIntoBST(root.left,ele)
    return root

def searchInBST(root,target):
    if root==None:
        return False
    elif root.data==target:
        return True
    elif root.data<target:
        return searchInBST(root.right,target)
    return searchInBST(root.left,target)

root=None
for ele in num:
    root=insertIntoBST(root,ele)

if searchInBST(root,target)==True:
    print("Target element is found")
else:
    print("Target element is not found")
