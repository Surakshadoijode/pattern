n=int(input())
l=list(map(int,input().split()))

def performBubbleSort(l):
    for fixThisRange in range(n-1,0,-1):
        for index in range(fixThisRange):
            if l[index]>l[index+1]:
                temp=l[index]
                l[index]=l[index+1]
                l[index+1]=temp
    
performBubbleSort(l)
print(*l)
