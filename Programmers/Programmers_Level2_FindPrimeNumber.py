## Programmers_Level2_Find Prime Number
## https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
## 09.14.2022

from itertools import permutations


# 소수 판별 함수
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:  # 나누어 떨어지면 소수가 아니다
            return False
    return True


def solution(numbers):
    # 소수: 1과 자기 자시난을 약수로 가지는 수
    answer = []  # 소수 몇개인지
    temp = []
    numbers = list(numbers)  # numbers를 리스트로 만들어주기 ['1', '7']

    for i in range(1, len(numbers) + 1):
        temp += list(permutations(numbers, i))
        # print("temp",temp)
    perList = [int(''.join(t)) for t in temp]

    for i in perList:
        if isPrime(i):  # true
            ## answer += 1 -> Nope. 중복이 있기 때문에
            answer.append(i)
        # print("answer",answer)

    return len(set(answer))
