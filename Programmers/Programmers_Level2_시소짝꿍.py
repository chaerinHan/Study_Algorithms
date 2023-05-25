## Programmers_Level2_양궁대회
## https://school.programmers.co.kr/learn/courses/30/lessons/92342
## 12.05.2023

from itertools import combinations_with_replacement


def solution(n, info):  # n: 화살 개수, info: 어피치가 과녁 점수
    answer = [-1]
    max_gap = -1  # 점수 차 일단 -1로 선언, 점수 차가 0일 수도 있으니
    arr = [1] * n
    # info.reverse()

    for case in combinations_with_replacement(range(11), n):
        peach, lion = 0, 0
        lions = [0] * 11

        # 라이언의 점수 배열에 넣기
        for i in case:  # case [0,0,0,0,0], [0,0,0,0,6] 이런식으로 화살이 있는 인덱스
            lions[10 - i] += 1  # case가 그냥 1로 되어있으니깐

        # 둘이 비교해서 더 많이 쏜 애가 이기기
        for i in range(11):
            if info[i] == lions[i] == 0:
                continue  # 둘 다 못 맞추면 그냥 넘어가기
            elif info[i] >= lions[i]:  # 비겨도 어피치 우승
                peach += 10 - i  # 어피치 승점 get
            else:
                lion += 10 - i

        if lion > peach:
            gap = lion - peach  # 라이언과 어피치의 점수 차
            if max_gap < gap:
                max_gap = gap  # 갭 최대 차이 갱신
                answer = lions

    return answer