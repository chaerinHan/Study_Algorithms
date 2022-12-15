## Programmers_Level3_Describe As N
## https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3
## 11.30.2022

def solution(N, number):
    answer = -1
    dp = []
    if number == 1:
        return 1

    for i in range(1, 9):
        # i = N의 개수
        all = set()
        # 이어 붙여서 만드는 경우
        all.add(int(str(N) * i))  # 5,55,555

        # print(dp)
        for j in range(i - 1):  # 1 ~ n-1, n-1 ~1까지의 사칙연산
            for op1 in dp[j]:
                print(dp[j])
                for op2 in dp[-j - 1]:
                    all.add(op1 - op2)
                    all.add(op1 + op2)
                    all.add(op1 * op2)
                    if op2 != 0:
                        all.add(op1 / op2)
        if number in all:  # number 존재하면
            answer = i
            break
        dp.append(all)

    return answer