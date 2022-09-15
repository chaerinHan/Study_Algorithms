## Programmers_Level2_H-Index
## https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=python3
## 09.01.2022
# reference: https://codermun-log.tistory.com/309

def solution(citations):
    answer = 0
    citations.sort()
    total = len(citations)
    for i in range(len(citations)):
        if citations[i] >= total-i:# h번 이상 인용된 논문이 h편 이상
            return total-i
    return 0