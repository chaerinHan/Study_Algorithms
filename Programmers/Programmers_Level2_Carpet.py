## Programmers_Level2_Carpet
## https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=python3
## 09.17.2022

def solution(brown, yellow):
    answer = []
    width = 0
    height = 0
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = int(yellow / i)
            h = i
        if (w * 2 + h * 2 + 4) == brown:
            answer.append(w + 2)
            answer.append(h + 2)
            print(sorted(answer, reverse=True))
            return sorted(answer, reverse=True)

    return answer)