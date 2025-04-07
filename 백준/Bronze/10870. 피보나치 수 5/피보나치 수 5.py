import sys

N = int(sys.stdin.readline())

if N == 0:
    print(0)
else:
    sulist = [0, 1]
    for i in range(2, N+1):
        sulist.append(sulist[i-1] + sulist[i-2])
    print(sulist[N])