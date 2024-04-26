target=int(input())
n=int(input())
num=list(map(int,input().split()))
found = False

left=0
right=len(num)-1
while left <= right:
    mid=(left + right)//2
    if num[mid] == target:
        found = True
        break
    elif num[mid] > target:
        right = mid - 1
    else:
        left = mid + 1

if found==True:
    print("Target is present")
else:
    print("Target is not present")
