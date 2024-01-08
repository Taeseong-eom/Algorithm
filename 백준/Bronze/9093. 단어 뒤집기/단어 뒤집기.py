import sys

input = sys.stdin.readline

LineNum = int(input())

for i in range(LineNum):
    li = list(input().split())
    for j in li:
        print(j[::-1], end=" ")