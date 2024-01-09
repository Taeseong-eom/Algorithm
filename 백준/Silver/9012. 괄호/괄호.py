import sys

input = sys.stdin.readline

LineNum = int(input())

for i in range(LineNum):
    line = input().strip()
    stack= []
    for j in line:
        if j == '(':
            stack.append(j)
        elif stack:
            stack.pop()
        else:
            print("NO")
            break
    else:
        print("YES" if not stack else "NO")


