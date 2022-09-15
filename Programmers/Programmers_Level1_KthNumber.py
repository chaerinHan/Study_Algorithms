## Programmers_Level1_Kth Number
## https://school.programmers.co.kr/learn/courses/30/lessons/42748
## 09.01.2022

def solution(array, commands):
    answer = []

    for i in commands:
        temp = array[i[0] - 1: i[1]]
        temp.sort()
        print(temp)
        answer.append(temp[i[2] - 1])

    return answer