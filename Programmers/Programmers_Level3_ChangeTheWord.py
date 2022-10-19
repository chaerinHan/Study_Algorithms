## Programmers_Level3_ChangeTheWord
## https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=python3
## 10.11.2022
from collections import deque


def solution(begin, target, words):
    answer = 0

    # 먼저 target이 words에 있는지 확인
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])  # 내가 가는 길과 현재 단어 넣기

    while queue:
        x, cnt = queue.popleft()  # 방금 뺀 단어, 이동한 횟수

        if x == target:
            answer = cnt
            return answer  # target 단어와 일치하면 횟수 리턴

        for i in range(0, len(words)):  # words를 돌면서
            temp_cnt = 0
            word = words[i]

            for j in range(len(x)):
                if x[j] != word[j]:
                    temp_cnt += 1
            if temp_cnt == 1:
                queue.append([word, cnt + 1])

    return answer