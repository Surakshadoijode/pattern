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
    newBlock=Node(val)
    if head==None:
        return newBlock
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newBlock
    newBlock.prev=tail
    return head

    
def addNodeAtHeadOfLinkedList(head,val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    newBlock.next = head
    head.prev = newBlock
    return newBlock

n=int(input())
l=list(map(int,input().split()))
element=int(input())
head=None
for ele in l:
    head=addNodeAtTailOfLinkedList(head,ele)
printLeftToRightManner(head)
printRightToLeftManner(head)

head=addNodeAtHeadOfLinkedList(head,element)
printLeftToRightManner(head)
printRightToLeftManner(head)
