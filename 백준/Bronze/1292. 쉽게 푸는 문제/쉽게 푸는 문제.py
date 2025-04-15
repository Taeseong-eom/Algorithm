import sys


line = sys.stdin.readline()
A, B = map(int, line.split())

su_list = []
for i in range(1, 50):
    for j in range(i):
        su_list.append(i)
sum = 0
for i in range(A-1, B):
    sum = sum + su_list[i]

print(sum)