#time complexity O(n)
l=[]
status=1
while status==1:
    print("Enter operations to perform 1. Insert 2. delete 3. display")
    x=int(input())
    if(x==1):
        i=int(input("Enter data : "))
        l.append(i)
    elif x==2:
        l.pop()
    elif x==3:
        print(l)
    
    print("Enter status 1. continue operations 2. exit")
    x=int(input())
    if x==1:
        status=1
    else:
        status=0
        
###############################
#time complexity O(1)
from collections import deque
stack=deque()
status=1
while status==1:
    print("Enter operations to perform 1. Insert 2. delete 3. display")
    x=int(input())
    if(x==1):
        i=int(input("Enter data : "))
        stack.append(i)
    elif x==2:
        stack.pop()
    elif x==3:
        print(stack)
    
    print("Enter status 1. continue operations 2. exit")
    x=int(input())
    if x==1:
        status=1
    else:
        status=0
m=list((stack))
m.sort()
print("Minimum element from stack : ",m[0])