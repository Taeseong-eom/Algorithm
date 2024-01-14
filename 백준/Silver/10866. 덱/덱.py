from collections import deque
import sys

input = sys.stdin.readline

CommandNum = int(input())
que = deque()

for i in range(CommandNum):
    CommandList = input().split()
    if CommandList[0] == 'push_front':
        que.appendleft(int(CommandList[1]))
    elif CommandList[0] == 'push_back':
        que.append(int(CommandList[1]))
    elif CommandList[0] == 'pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif CommandList[0] == 'pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif CommandList[0] == 'size':
        print(len(que))
    elif CommandList[0] == 'empty':
        if not que:
            print(1)
        else:
            print(0)
    elif CommandList[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif CommandList[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
