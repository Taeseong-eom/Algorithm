# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 예제 입력 1 
# 4 6
# 101111
# 101010
# 101011
# 111011
# 예제 출력 1 
# 15
# 예제 입력 2 
# 4 6
# 110110
# 110110
# 111111
# 111101
# 예제 출력 2 
# 9
# 예제 입력 3 
# 2 25
# 1011101110111011101110111
# 1110111011101110111011101
# 예제 출력 3 
# 38
# 예제 입력 4 
# 7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111
# 예제 출력 4 
# 13


import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]

# 상하좌우 이동
def bfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    
    # 방문 여부와 거리를 저장하는 배열
    visited = [[0] * M for _ in range(N)]
    visited[x][y] = 1  # 시작점 1 설정
    
    while queue:
        x, y = queue.popleft()
        
        # 도착점에 도달하면 거리 반환
        if x == N-1 and y == M-1:
            return visited[x][y]
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위를 벗어나지 않고, 이동할 수 있는 칸이며, 아직 방문하지 않은 경우
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    return visited[N-1][M-1]

# (0,0)에서 시작 (문제에서는 (1,1)로 주어졌지만 실제 인덱스는 0부터 시작)
print(bfs(0, 0))
