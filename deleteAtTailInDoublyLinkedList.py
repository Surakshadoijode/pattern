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

def deleteAtTailInLinkedlist(head):
    if head==None or head.next==None:
        return None
    curr=head
    previous=None
    while curr.next!=None:
        previous=curr
        curr=curr.next
    previous.next=None
    curr.prev=None
    return head

n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=addNodeAtTailOfLinkedList(head,ele)
printLeftToRightManner(head)
printRightToLeftManner(head)
head=deleteAtTailInLinkedlist(head)
printLeftToRightManner(head)
printRightToLeftManner(head)
