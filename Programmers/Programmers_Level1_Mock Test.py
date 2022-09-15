## Programmers_Level1_Mock Test
## https://school.programmers.co.kr/learn/courses/30/lessons/42840
## 09.14.2022

def solution(answers):
    count = [0, 0, 0]
    answer = []
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        # 수포자1 5개씩 반복
        if answers[i] == student1[i % 5]:
            count[0] += 1
        if answers[i] == student2[i % 8]:
            count[1] += 1
        if answers[i] == student3[i % 10]:
            count[2] += 1

    max_count = max(count)

    for i in range(3):
        if max_count == count[i]:
            answer.append(i + 1)  # 리스트는 0부터 시작하니깐

    return answer