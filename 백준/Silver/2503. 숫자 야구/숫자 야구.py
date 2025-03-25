import sys
from itertools import permutations

N = int(sys.stdin.readline())
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0

for nums in permutations(range(1, 10), 3):
    num_str = ''.join(map(str, nums))
    flag = True

    for q_num, s, b in questions:
        q_num_str = str(q_num)
        strike = 0
        ball = 0

        for i in range(3):
            if num_str[i] == q_num_str[i]:
                strike += 1
            elif num_str[i] in q_num_str:
                ball += 1

        if strike != s or ball != b:
            flag = False
            break

    if flag:
        cnt += 1

print(cnt)
