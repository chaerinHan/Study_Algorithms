## Programmers-Level2.Hotter
## https://school.programmers.co.kr/learn/courses/30/lessons/42626?language=python3
## 08.24.2022

import heapq ## heap 만들어주는 모듈

def solution(scoville, K):
    ## 가장 작은 것, 두번째로 가장 작은 것을 계속 찾기
    heapq.heapify(scoville)
    mixed = 0
    answer = 0
    while scoville[0] < K:
        # mixed 만들때 아예 pop해버리기
        mixed = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville,mixed) # 새로 만든 것 추가하기
        answer += 1 # 섞는 과정 +1
        if scoville[0] < K and len(scoville) == 1: ## len(scoville)=1 : 모든 음식 K이상 못만든 경우
            return -1
    return answer