## Programmers_Level2_시소짝꿍
## https://school.programmers.co.kr/learn/courses/30/lessons/152996
## 12.05.2023

from collections import defaultdict


def solution(weights):
    answer = 0
    # 탑승한 사람의 무게 = 시소 축 * 좌석 간의 거리 곱 => 시소 짝꿍
    # 시소 짝꿍 1:1, 1:2, 2:3, 3:4

    info = defaultdict(int)  # 빈 defaultdict 만들어주기

    for weight in weights:
        answer += info[weight] + info[weight * 2] + info[weight * 1 / 2] + info[weight * 3 / 4] + info[weight * 4 / 3] + \
                  info[weight * 2 / 3] + info[weight * 3 / 2]

        info[weight] += 1
    return answer