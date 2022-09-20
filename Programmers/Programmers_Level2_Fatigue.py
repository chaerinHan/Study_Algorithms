## Programmers_Level2_Fatigue
## https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3
## 09.17.2022

from itertools import permutations


def solution(k, dungeons):
    # k: 현재 피로도, dungeons: [["최소 필요 피로도", "소모 피로도"]] min >= req
    answer = 0
    temp = []

    # dungeons의 순서를 바꿔주야함
    #temp += permutations(dungeons, len(dungeons))
    print(permutations(dungeons, len(dungeons)))
    for i in permutations(dungeons, len(dungeons)):
        count = 0 # 통과한 던전 수
        fatigue = k # 현재 피로도
        for j in i:
            minF = j[0]
            useF = j[1]
            if fatigue >= minF:
                fatigue -= useF
                count += 1
        answer = max(answer,count)
    return answer