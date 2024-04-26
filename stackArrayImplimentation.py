def push(stack,val):
    stack.insert(0,val)
    print(val,"inserted")

def pop(stack):
    if len(stack)==0:
        print("Stack is empty")
        return
    print(stack[0], "deleted")
    stack.pop(0)

def printStack(stack):
    if len(stack)==0:
        print("Stack empty")
        return
    print(stack)
    
stack = []
n = int(input().strip())
while n > 0:
    word = list(map(int, input().split()))
    l = word[0]
    if l == 1:
        num = word[1]
        stack.insert(0, num)
        print(num, "inserted")
    elif l == 2:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print(stack[0])
    elif l == 3:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print(stack[0])
            stack.pop(0)
    elif l == 4:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            for ele in stack:
                print(ele, end = " ")
            print()
    else:
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
      
    n -= 1
