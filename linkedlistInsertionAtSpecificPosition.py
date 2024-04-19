class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data,end=" -->")
        curr=curr.next
    print("None")

def insertAtEnd(head,ele):
    new=Node(ele)
    if head==None:
        return new
    curr = head
    while curr.next!=None:
        curr=curr.next
    curr.next=new
    return head

def insertAtSpecificPosition(head,position,value):
    new=Node(value)
    index=1
    curr=head
    while index!=position-1:
        curr=curr.next
        index=index+1
    new.next=curr.next
    curr.next=new
    return head

l = [11,22,33,44,55,] 
head=None
for ele in l:
    head=insertAtEnd(head,ele)
head=insertAtSpecificPosition(head,2,300)  
printLinkedList(head)
