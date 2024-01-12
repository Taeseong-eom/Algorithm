import sys
from collections import deque
input = sys.stdin.readline

CommandNum = int(input()) # 명령어 수
Q = deque()
result = []
for i in range(CommandNum):
    command = input().split()
    if command[0] == 'push':
        Q.append(int(command[1]))
    elif command[0] == 'pop':
        if Q:
            result.append(Q.popleft())
        else:
            result.append(-1)
    elif command[0] == 'size':
        result.append(len(Q))
    elif command[0] == 'empty':
        if Q:
            result.append(0)
        else:
            result.append(1)
    elif command[0] == 'front':
        if Q:
            result.append(Q[0])
        else:
            result.append(-1)
    elif command[0] == 'back':
        if Q:
            result.append(Q[-1])
        else:
            result.append(-1)
for i in result:
    print(i)