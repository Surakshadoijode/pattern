class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def printLeftToRightManner(head):
    curr = head 
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next 
    print()

def printRightToLeftManner(head):
    tail = head 
    while tail.next != None:
        tail = tail.next 
    curr = tail
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.prev 
    print()

def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
    tail = head
    while tail.next != None:
        tail = tail.next
    tail.next = newBlock
    newBlock.prev = tail
    return head

def addNodeAtSpecificPosition(head, position, val):
    newBlock = Node(val)
    if position == 1:
        newBlock.next = head
        if head != None:
            head.prev = newBlock
        return newBlock
    if head == None:
        return newBlock
    index = 1
    curr = head
    while index != position - 1 and curr.next != None:
        index += 1
        curr = curr.next
    nextNode = curr.next
    newBlock.next = nextNode 
    if nextNode != None:
        nextNode.prev = newBlock
    curr.next = newBlock 
    newBlock.prev = curr 
    return head

n = int(input())
l = list(map(int, input().split()))
position,val = map(int,input().split())
head = None
for ele in l:
    head = addNodeAtTailOfLinkedList(head, ele)
printLeftToRightManner(head)
printRightToLeftManner(head)
head = addNodeAtSpecificPosition(head, position, val)
printLeftToRightManner(head)
printRightToLeftManner(head)
