## Programmers_Level3_징검다리 건너기
## https://school.programmers.co.kr/learn/courses/30/lessons/64062
## 11.05.2023

def solution(stones, k):  # k 뛸 수 있는 최대 칸
    answer = 0

    start, end = 1, max(stones)

    while start <= end:
        mid = (start + end) // 2
        jump = 0
        for stone in stones:
            if stone - mid <= 0:
                jump += 1
            else:
                jump = 0  # 다시 초기화 해주기

            if jump >= k:
                break
        if jump >= k:
            end = mid - 1
        else:
            start = mid + 1

    return start