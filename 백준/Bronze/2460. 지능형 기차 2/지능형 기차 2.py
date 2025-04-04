import sys

data = sys.stdin.readlines()

count = 0
station = []

for i in data:
    line = i.split()
    minus = int(line[0])
    plus = int(line[1])
    count = count - minus + plus
    station.append(count)

print(max(station))