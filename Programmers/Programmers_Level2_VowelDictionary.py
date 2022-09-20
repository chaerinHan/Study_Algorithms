## Programmers_Level2_Vowel Dictionary
## https://school.programmers.co.kr/learn/courses/30/lessons/84512
## 09.17.2022


from itertools import product


def solution(word):
    answer = 0
    dict = []
    vowel = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6):
        for v in product(vowel, repeat=i):
            dict.append(''.join(list(v)))

    dict.sort()
    return dict.index(word) + 1