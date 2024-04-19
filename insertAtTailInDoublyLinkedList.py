class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def printLeftToRight(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()

def printRightToLeft(head):
    tail=head
    while tail.next!=None:
        tail=tail.next

    curr=tail
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.prev
    print()

def insertAtTailDoublyLinkedList(head,val):
    newBlock=Node(val)
    if head==None:
        return newBlock
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newBlock
    newBlock.prev=tail
    return head

n=int(input())
l=list(map(int,input().split()))
val=int(input())
head=None
for ele in l:
    head=insertAtTailDoublyLinkedList(head,ele)
printLeftToRight(head)
printRightToLeft(head)
head=insertAtTailDoublyLinkedList(head,val)
printLeftToRight(head)
printRightToLeft(head)
