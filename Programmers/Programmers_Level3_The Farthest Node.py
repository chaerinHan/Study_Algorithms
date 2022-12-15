## Programmers_Level3_The Farthest Node
## https://school.programmers.co.kr/learn/courses/30/lessons/49189?language=python3
## 11.30.2022

from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]  # n은 노드의 개수
    minDistance = [-1] * (n + 1)  # 각 노드의 최단 거리 리스트, 방문 리스트

    # 1 노드 연결해주기
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    # graph : 	[[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]

    q = deque([1])  # 시작 노드는 1
    minDistance[1] = 0  # 출발 노드는 거리 0

    # print(q)
    # print(".")
    # print(minDistance)
    # BFS
    while q:
        now = q.popleft()  # 현재 노드

        for i in graph[now]:
            if minDistance[i] == -1:  # 아직 방문 안했으면
                q.append(i)  # queue에 추가
                # print(q)
                # print("..")
                minDistance[i] = minDistance[now] + 1  # 그 노드까지의 거리 + 1
                # print(minDistance)

    for j in minDistance:
        if j == max(minDistance):
            answer += 1

    return answer