## Programmers_Level3_Ranking
## https://school.programmers.co.kr/learn/courses/30/lessons/49191?language=python3
## 11.30.2022

from collections import defaultdict


def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    # [a > b] a 가 b 이김
    for w, l in results:
        # 나를 이긴 사람
        win[l].add(w)
        # 나에게 진 사람
        lose[w].add(l)

    for i in range(1, n + 1):
        # i가 이긴 애는 i한테 진 애들도 다 i가 이긴 상대
        for l in lose[i]:
            win[l].update(win[i])
        # i한테 진 애들은 i가 이긴 애들한테도 진 것
        for w in win[i]:
            lose[w].update(lose[i])

    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:  # 본인 제외
            answer += 1

    return answer