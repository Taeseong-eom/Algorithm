import sys
from collections import deque
input = sys.stdin.readline

CommandNum = int(input()) # 명령어 수
numlist = list(map(int, input().split()))

오큰수 = [-1]*CommandNum

stack = deque()

for i in range(CommandNum):
    while stack and numlist[stack[-1]] < numlist[i]:
        오큰수[stack.pop()] = numlist[i]
    stack.append(i)
print(*오큰수)