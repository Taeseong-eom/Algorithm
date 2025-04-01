import sys

line = list(map(int, sys.stdin.readline().split()))

N = line[0]
K = line[1]

yaksu = []

for i in range(1, N+1):
    if (N % i)==0:
        yaksu.append(i)

if len(yaksu) < K:
    print(0)
else:
    print(yaksu[K-1])
