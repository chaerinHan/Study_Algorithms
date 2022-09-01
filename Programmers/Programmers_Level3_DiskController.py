## Programmers_Level3_DiskController
## https://school.programmers.co.kr/learn/courses/30/lessons/42627?language=python3
## 08.24.2022

import heapq


def solution(jobs):
    # 평균을 가장 줄이는 방법 (요청~종료)
    # 최솟값을 찾아서 계속 더하기 but 앞에 일정이 끝난후

    # start: 바로 이전에 완료한 작업의 시작 시간
    start = -1
    answer, i, now = 0, 0, 0
    heap = []

    # 현재 시점에서 처리할 수 있는 작업들 heap에 저장
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:  # job[0]: 작업 요청 시점 [1]: 걸리는 시간
                heapq.heappush(heap, [job[1], job[0]])  # [소요시간, 요청 시점]

        if len(heap) > 0:  # 작업요청heap이 들어오면, 처리할 작업이 있으면
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])  # 작업 요청 시간부터 종료시간까지의 시간
            i += 1
        else:  # 처리할 작업 없는 경우
            now += 1

    return (answer // len(jobs))