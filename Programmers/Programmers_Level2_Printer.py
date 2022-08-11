## Programmers-Level2.Printer
## https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3
## 08.11.2022

def solution(priorities, location):
    # location: 요청한 문서가 현재 어떤 위치에 있는지
    answer = 0
    result = []

    # 인덱스 저장하는 리스트
    turns = [i for i in range(len(priorities))]
    print("idx:", turns)

    turn = 0
    while len(priorities) != 0:
        if priorities[0] == max(priorities):  # 현재 순서가 최고우선순위라면 프린트
            priorities.pop(0)  # 프린트했으니 pop
            result.append(turns.pop(0))  # 정답 리스트에 idx의 첫번째 항목 추가(프린트 했으니)

        # 우선순위 밀린 상태
        else:
            priorities.append(priorities.pop(0))  # 앞에 항목 꺼내서 맨 뒤에 넣기
            turns.append(turns.pop(0))

    return result.index(location) + 1  # 리스트니깐 순서로는 index +1

