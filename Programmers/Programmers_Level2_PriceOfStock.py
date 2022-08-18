## Programmers-Level2.Price Of Stock
## https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3
## 08.18.2022

def solution(prices):
    answer = [0] * len(prices)
    time = len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:  # 주가 상승
                answer[i] += 1
            else:
                answer[i] += 1
                break

    return answer