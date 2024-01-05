import sys

input = sys.stdin.readline
n = int(input())
stack = []
lst = []
for i in range(n):
    lst.append(input())

for l in lst:
    if 'push' in l.split()[0]:
        stack.append(int(l.split()[1]))

    elif 'top' in l:
        # 스택이 비어있지 않으면 스택의 가장 위의 값을 출력
        # 스택이 비어있으면 -1을 출력
        if stack:
            print(stack[-1])
        else:
             print(-1)

    elif 'size' in l:
        # 스택의 크기를 출력
        print(len(stack))
    
    elif 'empty' in l:
        # 스택이 비어있지 않으면 0을 출력
        # 스택이 비어있으면 1을 출력
    
        if stack: 
            print(0) 
        else:
            print(1)

    elif 'pop' in l:
        # 스택이 비어있지 않으면 가장 위의 값을 스택에서 빼내어 출력
        # 스택이 비어있으면 -1을 출력
        if stack:
            print(stack.pop())  
        else: 
            print(-1)