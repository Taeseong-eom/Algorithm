# 문제
# 전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.

# N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

# 입력
# 첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

# 출력
# 첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.

# 예제 입력 1 
# 5 5
# WBWWW
# WWWWW
# BBBBB
# BBBWW
# WWWWW
# 예제 출력 1 
# 130 65


import sys
from collections import deque

line1 = sys.stdin.readline()

N, M = map(int, line1.split()) # 전쟁터의 가로 크기 N, 세로 크기 M

white_power = 0
blue_power = 0

# 전쟁터 배열 생성
war_field = [[0] * N for _ in range(M)]

for i in range(M):
    line = sys.stdin.readline()
    for j in range(N):
        war_field[i][j] = line[j]

visited = [[False] * N for _ in range(M)]

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, team):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if not visited[nx][ny] and war_field[nx][ny] == team:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
                    
    return count

# 모든 위치를 순회하면서 각 팀의 위력을 계산
for i in range(M):
    for j in range(N):
        if not visited[i][j]:
            if war_field[i][j] == 'W':
                count = bfs(i, j, 'W')
                white_power += count * count
            else:
                count = bfs(i, j, 'B')
                blue_power += count * count

print(white_power, blue_power)


