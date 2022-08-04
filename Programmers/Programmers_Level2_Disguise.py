## Programmers-Level2.Disguise
## https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=python3
## 07.26.2022

# [프로그래머스 - 위장]

def solution(clothes):
    answer = 0
    closet = {}  # 빈 딕셔너리 생성
    # cloth[0]: 옷 이름, cloth[1]: 옷 종류
    ## 같은 종류끼리 딕셔너리에 넣기
    for cloth in clothes:
        if cloth[1] in closet.keys():
            closet[cloth[1]].append(cloth[0])  # 포함하고 있으면 key값에 추가
        else:
            closet[cloth[1]] = [cloth[0]]  # 없으면 그냥 넣기

    for num in closet.values():
        answer *= len(num) + 1  # 해당 옷 종류를 안 입는 것도 경우의 수

    return answer - 1  # 다 벗고 있는 경우 제외