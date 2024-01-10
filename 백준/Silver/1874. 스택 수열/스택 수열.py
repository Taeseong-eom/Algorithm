import sys

input = sys.stdin.readline

LineNum = int(input())
stack= []
출력배열 = []
count = 1
state = True

for i in range(LineNum):
    line = int(input())
    while count <= line:
        stack.append(count)
        출력배열.append("+")
        count+=1
    if stack[-1]==line:
        출력배열.append("-")
        stack.pop()
    else:
        state = False
        break
if state == False:
    print("NO")
else:
    for i in 출력배열:
        print(i)