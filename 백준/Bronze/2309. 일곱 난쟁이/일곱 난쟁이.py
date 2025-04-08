import sys

data = sys.stdin.readlines()

lines = list(map(int, data))
result = []

for i in range(9):
    for j in range(i+1, 9):
        if sum(lines) - lines[i] - lines[j] == 100:
            result = [lines[k] for k in range(9) if k != i and k != j]
            result.sort()
            for num in result:
                print(num)
            exit()