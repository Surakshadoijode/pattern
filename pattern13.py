n=int(input())
constant=10
for i in range(1,n+1):
    for j in range(i):
        print(constant,end=" ")
        constant=constant+10
    print()
