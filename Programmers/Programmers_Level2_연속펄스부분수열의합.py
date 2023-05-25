## Programmers_Level2_연속펄스부분수열의
## https://school.programmers.co.kr/learn/courses/30/lessons/161988
## 17.05.2023

def solution(sequence):
    answer = 0
    pulse = [1, -1]
    dp = [[0, 0] for _ in range(len(sequence))]
    dp[0] = [sequence[0], sequence[0]]

    for i in range(1, len(sequence)):
        num = sequence[i] * pulse[i % 2]
        # 최소값
        dp[i][0] = min(num, num + dp[i - 1][0])
        # 최대값
        dp[i][1] = max(num, num + dp[i - 1][1])

    min_dp = min(map(min, dp))
    max_dp = max(map(max, dp))

    answer = max(abs(min_dp), abs(max_dp))
    return answer