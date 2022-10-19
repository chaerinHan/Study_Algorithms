## Programmers_Level3_Trip Route
## https://school.programmers.co.kr/learn/courses/30/lessons/43164?language=python3
## 10.12.2022

from collections import deque
from collections import defaultdict


def solution(tickets):
    answer = []

    tickets.sort(key=lambda x: (x[1], x[0]))  # 도착지의 알파벳순으로

    tic = defaultdict(list)

    for [depart, arrive] in tickets:
        tic[depart].append(arrive)  # 출발지별 dict 만들기

    # 출발 - 도착 역순으로 정렬
    for k in tic.keys():
        tic[k].sort(reverse=True)  # tic[k]의 키값들이 역순으로

    def dfs():
        stack = ["ICN"]

        while stack:

            start = stack[-1]  # [ICN]

            if not tic[start]:  # tic에 start로 시작하는게 없으면
                answer.append(stack.pop())
            else:  # start로 시작하는게 있으면
                stack.append(tic[start].pop())  # 도착지 넣어
                # 그러면 다시 도착지가 출발지가 되면서 계속 반복

    dfs()
    return answer[::-1]  # 끝에 ICN 빼주기