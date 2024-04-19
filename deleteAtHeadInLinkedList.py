class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printLinkedList(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    print()

def insertAtTailLinkedList(head,ele):
    newBlock=Node(ele)
    if head==None:
        return newBlock
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=newBlock
    return head

def deleteAtHeadLinkedList(head):
    if head==None:
        return None
    secondNode=head.next
    head.next=None
    return secondNode

n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtTailLinkedList(head,ele)
printLinkedList(head)
head=deleteAtHeadLinkedList(head)
printLinkedList(head)
