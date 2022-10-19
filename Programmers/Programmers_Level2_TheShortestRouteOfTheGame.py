## Programmers_Level2_The Shortes Route of The Game
## https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3
## 10.11.2022
 
from collections import deque # 너비우선탐색
def solution(maps):
    answer = 0

    # 방향 정의 [상하좌우]
    dx = [-1, 1, 0, 0] # 행 이동
    dy = [0, 0, -1, 1] # 열 이동

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        # queue가 빌 때까지 반복, 큐에서 꺼내기
        while queue:
            x, y = queue.popleft() # 현재 캐릭터 좌표

            # 상하좌우 칸 확인하기
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵을 벗어나면 무시하기
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue

                # 0이면 벽 -> 벽이면 무시하기
                if maps[nx][ny] == 0:
                    continue

                # 처음 지나가는 길이면 거리계산하고 다시 상하좌우 확인하기
                if maps[nx][ny] == 1:
                    # 인접한 칸에 원래 좌표의 값에 1을 더하여 할당
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny)) # 다시 큐에 넣어서 또 상하좌우 확인하게

        # 상대 팀 진영(제일 오른쪽 아래 칸)까지의 거리 반환
        return maps[len(maps)-1][len(maps[0])-1]

    answer = bfs(0, 0) # 현재 좌표 (0,0)
    return -1 if answer == 1 else answer    # 상대 팀 진영에 도착할 수 없을 때 -1