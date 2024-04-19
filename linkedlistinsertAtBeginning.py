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

def insertAtBeginning(head,ele):
    new=Node(ele)
    if head==None:
        return new
    new.next=head
    return new

l = [11,22,33,44,55] 
head=None
for ele in l:
    head=insertAtBeginning(head,ele)    
printLinkedList(head)
