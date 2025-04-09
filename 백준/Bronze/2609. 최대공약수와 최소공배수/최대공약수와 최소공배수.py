# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 예제 입력 1 
# 24 18
# 예제 출력 1 
# 6
# 72

import sys


data = sys.stdin.readline()

line = list(map(int,data.split()))

N, M = line[0], line[1]  # 두 개의 자연수
 
N의약수 = []
M의약수 = []

for i in range(1, N+1):
    if N % i == 0:
        N의약수.append(i)
for i in range(1, M+1):
    if M % i == 0:
        M의약수.append(i)
공약수=[]
for i in N의약수:
    for j in M의약수:
        if i == j:
            공약수.append(i)

최대공약수 = max(공약수)

최소공배수 = (N * M) // 최대공약수

print(str(최대공약수) + "\n" + str(최소공배수))

