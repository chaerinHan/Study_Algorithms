## Programmers_Level3_Pick Up The Item
## 10.19.2022

from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    # 테두리까지 해서 좌표를 2배로
    field = [[5] * 102 for i in range(102)]  # 테두리가 -1

    # 직사각형 그리기
    for a in rectangle:
        # 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x * 2, a)  # a만큼 그 입력값들을 x*2

        # x1부터 x2, y1부터 y2까지 순회
        for i in range(x1, x2 + 1):  # x1 ~ x2까지 해야하니 x2 + 1
            for j in range(y1, y2 + 1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:
                    field[i][j] = 1

    print(field)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    # 출발지점 넣어주기
    q.append([characterX * 2, characterY * 2])

    # 최단거리용 방문 배열
    visited = [[1] * 102 for i in range(102)]

    while q:
        x, y = q.popleft()

        # 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2  # 맵이 2배니깐 다시 2로 나누기
            break

        # 아니면 방향 돌면서
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])  # q에 추가
                visited[nx][ny] = visited[x][y] + 1  # 좌표에 거리 1 추가

    return answer