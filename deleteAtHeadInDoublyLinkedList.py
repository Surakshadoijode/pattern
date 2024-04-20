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

def deleteAtHeadOfDoublyLinkedList(head,ele):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    secondNode.prev=None
    return secondNode
    
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=addNodeAtTailOfLinkedList(head,ele)
printLeftToRightManner(head)
printRightToLeftManner(head)
head=deleteAtHeadOfDoublyLinkedList(head,ele)
printLeftToRightManner(head)
printRightToLeftManner(head)
