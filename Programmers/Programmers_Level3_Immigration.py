## Programmers_Level3_Immigration
## https://school.programmers.co.kr/learn/courses/30/lessons/43238
## 11.23.2022

def solution(n, times):
    answer = 0
    # n: 인원, times: [걸리는 시간]
    # 정렬하기
    times.sort()

    left, right = 1, max(times) * n  # right: 가장 비효율적으로 걸리는 시간(n명에게 모두 검사)

    while left <= right:
        mid = (left + right) // 2  # mid: 모든 심사관들에게 심사 받는 시간
        ppl = 0
        for i in times:
            ppl += mid // i  # 모든 심사관들이 mid 시간동안 심사한 사람의 수
            # 모든 심사관 거치지 않았음에도
            if ppl >= n:
                break  # 목표치 사람 넘겼으면 나오기

        if ppl >= n:
            answer = mid
            right = mid - 1
        elif ppl < n:
            left = mid + 1

    return answer