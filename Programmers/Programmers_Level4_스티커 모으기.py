## Programmers_Level4_스티커 모으기
## https://school.programmers.co.kr/learn/courses/30/lessons/12971
## 11.05.2022


def solution(sticker):
    # DP - 점화식 이용해서 푸는 것
    answer = 0
    # 스티커 하나면 그냥 그거
    if len(sticker) == 1:
        return sticker[0]
    table = [0 for _ in range(len(sticker))]
    # table[i] = i번째까지의 최대값
    table2 = table

    # 0번에서 시작 - 마지막꺼 못 떼어요
    table[0] = sticker[0]  # 자신 스티커


    table[1] = table[0]
    for i in range(2, len(sticker) - 1):
        table[i] = max(sticker[i] + table[i - 2], table[i - 1])
    value = max(table)

    # 1번에서 시작 - 마지막꺼 뗄 수 있어요
    table2[0] = 0  # 1번부터 시작이니
    table2[1] = sticker[1]
    for i in range(2, len(sticker)):
        table2[i] = max(table2[i - 1], sticker[i] + table[i - 2])
    return max(value, max(table2))