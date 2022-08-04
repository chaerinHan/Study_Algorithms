## Programmers-Level1.Who Did Not Complete
## https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3
## 07.26.2022

# [프로그래머스 - 완주하지 못한 선수]

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for part, comp in zip(participant, completion):
        if part != comp:
            return part
    return participant[-1]
## completion을 다 돌고도 안나오면 part 끝에 있다는 것 -> participant 맨 뒤에를 return / 2