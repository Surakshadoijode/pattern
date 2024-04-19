class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
def printLinkedList(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
    
def insertAtEnd(head,ele):
    new=Node(ele)
    if head==None:
        return new
    curr=head
    while curr.next!=None:
        curr=curr.next
    curr.next=new
    return head

def deleteAtTail(head):
    if head==None:
        return None
    curr=head
    previous=None
    while curr.next!=None:
        previous=curr
        curr=curr.next
    if previous==None:
        return None
    else:
        previous.next=None
        return head
    
num=int(input())
l=list(map(int,input().split()))

head=None
for ele in l:
    head=insertAtEnd(head,ele)
    
printLinkedList(head)
print()

head=deleteAtTail(head)
printLinkedList(head)
