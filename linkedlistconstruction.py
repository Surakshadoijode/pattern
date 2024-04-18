class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printLinkedList(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
def insertAtTail(head,ele):
    new=Node(ele)
    if head==None:
        return new
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=new
    return head

n=int(input())
l=list(map(int,input().split()))

head=None
for ele in l:
    head=insertAtTail(head,ele)
printLinkedList(head)
