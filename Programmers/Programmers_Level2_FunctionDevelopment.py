## Programmers-Level2.FunctionDevelopment
## https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=python3
## 08.10.2022

def solution(progresses, speeds):
    answer = []

    while progresses:
        # 작업 리스트의 진도 속도 더해주기
        for i in range(len(progresses)):  # Progresses 돌면서 진행 속도를 더해주기
            progresses[i] += speeds[i]

        count = 0  ## 배포하는 기능 카운트

        ## Progresses 리스트가 남아있으면서 작업 진도가 100이상인 경우 -> 배포 기능 +1
        while progresses and progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)

        # 배포할게 있으면
        if count > 0:
            answer.append(count)  # 배포하는 기능 개수 answer에 추가

    return answer