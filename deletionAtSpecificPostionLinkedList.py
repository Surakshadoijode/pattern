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

def deleteAtSpecificPosition(head,position):
    curr=head
    index=1
    while index!=position-1:
        curr=curr.next
        index=index+1
    mainNode=curr.next
    nextNode=mainNode.next
    mainNode.next=None
    curr.next=nextNode
    return head

n=int(input())
l=list(map(int,input().split()))
head=None
position=int(input())
for ele in l:
    head=insertAtTailLinkedList(head,ele)
printLinkedList(head)
head=deleteAtSpecificPosition(head,position)
printLinkedList(head)
