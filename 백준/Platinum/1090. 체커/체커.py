n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]
answer = [int(1e9)] * n 

for x in coordinates: 
    for y in coordinates:
        costs = []
        for ix, iy in coordinates: 
            costs.append(abs(x[0] - ix) + abs(y[1] - iy))

        costs.sort()
        cost = 0
        for i in range(n):
            cost += costs[i]
            answer[i] = min(answer[i], cost)

print(*answer)