## Programmers_Level1_The Minimum Of Rectangles
## https://school.programmers.co.kr/learn/courses/30/lessons/86491
## 09.14.2022

def solution(sizes):
    answer = 0
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else: # sizes[i][0] < sizes[i][1]
            h.append(sizes[i][0])
            w.append(sizes[i][1])
    return max(w) * max(h)