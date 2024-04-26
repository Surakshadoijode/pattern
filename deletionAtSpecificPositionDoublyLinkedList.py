class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

def printLeftToRightManner(head):
    curr = head 
    while curr!= None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()

def printRightToLeftManner(head):
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()
    
def addNodeAtTailOfLinkedList(head,val):
    new=Node(val)
    if head==None:
        return new
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=new
    new.prev=tail
    return head

def deleteAtSpecificPositionLinkedList(head,position):
    curr=head
    index=1
    while index!=position-1:
        curr=curr.next
        index=index+1
    nodeToBeDeleted=curr.next
    nextNode=nodeToBeDeleted.next
    curr.next=nextNode
    nextNode.prev=curr
    return head

n=int(input())
l=list(map(int,input().split()))
position=int(input())
head=None
for ele in l:
    head=addNodeAtTailOfLinkedList(head,ele)
printLeftToRightManner(head)
printRightToLeftManner(head)
head=deleteAtSpecificPositionLinkedList(head,position)
printLeftToRightManner(head)
printRightToLeftManner(head)

