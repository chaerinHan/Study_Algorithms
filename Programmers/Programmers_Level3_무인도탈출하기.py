## Programmers_Level3_무인도탈출하기
## https://school.programmers.co.kr/learn/courses/30/lessons/154540
## 18.05.2023

from collections import deque
import sys

from collections import deque

posx = [1, -1, 0, 0]
posy = [0, 0, 1, -1]


def bfs(maps, visit, borderx, bordery, i, j):
    visit[i][j] = 1
    q = deque()
    q.append([i, j])
    days = 0
    while q:
        i, j = q.popleft()
        days += int(maps[i][j])
        for d in range(4):
            x, y = i + posx[d], j + posy[d]
            if not (0 <= x < borderx and 0 <= y < bordery): continue
            if visit[x][y] == 0 and maps[x][y] != 'X':
                q.append([x, y])
                visit[x][y] = 1
    return days
    """
    q = deque()
    visit[i][j] = 1 # 방문 처리
    q.append([i,j]) # 현재 좌표 넣기
    days = 0

    while q:
        curx, cury = q.popleft() # 현재 좌표 꺼내기
        #days += int(maps[i][j]) # 지도의 날짜 누적 (생존 가능일)
        print(maps[i][j])
        for i in range(4):
            newx = curx + posx[i]
            newy = cury + posy[i]

            # 맵 규격 벗어나면 break
            if not( 0<= newx < borderx and 0<= newy < bordery):
                continue
            if visit[newx][newy] == 0 and maps[newx][newy] != 'X':
                q.append([newx,newy])
                visit[newx][newy] = 1
    return days"""


def solution(maps):
    answer = []

    for i in range(len(maps)):
        maps[i] = list(maps[i])
    print(maps)

    bordery = len(maps[0])
    borderx = len(maps)

    # visit = [ [0] * len(maps[0])] * len(maps)
    visit = [[0] * bordery for _ in range(borderx)]

    for i in range(borderx):
        for j in range(bordery):
            # MAP이 x가 아니고, 방문하지 않은곳이 라면
            if maps[i][j] != 'X' and visit[i][j] == 0:
                answer.append(bfs(maps, visit, borderx, bordery, i, j))

    if answer:
        return sorted(answer)
    else:
        return [-1]

    return answer


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))