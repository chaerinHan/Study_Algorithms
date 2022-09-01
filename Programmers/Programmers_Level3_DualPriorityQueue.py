## Programmers_Level3_dual priority queue
## https://school.programmers.co.kr/learn/courses/30/lessons/42628?language=python3
## 09.01.2022
# reference: https://codermun-log.tistory.com/309
import heapq
def solution(operations):
    min_heap = []
    for value in operations:
        order, data = value.split()
        data = int(data)
        # 최댓값 삭제
        if order == "D" and data == 1:
            if min_heap:
                max_value = max(min_heap)
                min_heap.remove(max_value)
        # 최솟값 삭제
        elif order == "D" and data == -1:
            if min_heap:
                heapq.heappop(min_heap)
        # 큐 데이터 삽입
        else:
            heapq.heappush(min_heap, data)

    # heap이 비어있는 경우
    if not min_heap:
        return [0, 0]
    return max(min_heap), min_heap[0]wer