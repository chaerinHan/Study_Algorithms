## Programmers_Level2_The Biggest Number
## https://school.programmers.co.kr/learn/courses/30/lessons/42746
## 09.01.2022

def solution(numbers):

    answer = ''
    num = list(map(str, numbers))
    print(num)
    num.sort(key = lambda x : x*3, reverse = True) # ['6', '2', '10']

    return str(int(''.join(num)))r