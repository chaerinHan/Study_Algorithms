## Programmers_Level2_Lifeboat
## https://school.programmers.co.kr/learn/courses/30/lessons/42885
## 11.02.2022

from collections import deque


def solution(people, limit):
    answer = 0

    people = deque(sorted(people, reverse=True))

    while len(people) > 1:
        if people[0] + people[-1] <= limit:  # 무거운애, 가벼운애 태우기
            answer += 1
            people.pop()  # 제일 가벼운애 pop
            people.popleft()  # 제일 무거운애 pop
        else:  # limit 초과해버리면
            answer += 1
            people.popleft()  # 그냥 무거운애만 빼서 보트 태워버려

    if len(people) > 0:  # 애가 하나라도 남아있으면 그냥 보트 태워버려
        print(people)
        answer += 1

    return answer