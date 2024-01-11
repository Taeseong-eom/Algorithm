import sys

input = sys.stdin.readline

string = input().strip() # 초기 문자열
CommendNum = int(input()) #입력 명령어 수
left_stack = list(string)
right_stack = []

for _ in range(CommendNum):
    commend = input().split()
    if commend[0] == 'P':
        left_stack.append(commend[1])
    elif commend[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif commend[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    else: # 'B' 명령어 처리
        if left_stack:
            left_stack.pop()

print("".join(left_stack + right_stack[::-1]))