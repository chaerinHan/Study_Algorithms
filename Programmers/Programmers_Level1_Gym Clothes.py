## Programmers_Level1_Gym Clothes
## https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=python3
## 10.26.2022

def solution(n, lost, reserve):
    # 여벌 체육복 있는 애: 1이상 n이하
    # 여벌 있는 애도 도둑 맞을 수 있음 -> 체육복 못 빌려줘
    # 도난 당한 애 앞/뒤 확인해서 여벌 있는지 확인

    answer = 0
    # lost : 도단당한 애들 reserve: 여벌 있는 애들

    # 여벌 옷있는 애들중 도난당한 애들 제외
    r_set = set(reserve) - set(lost)  # -> 옷 빌려줄 수 있는 애들
    print(r_set)
    # 도난당한 애들중 여벌 옷 있는 애 제외
    l_set = set(lost) - set(reserve)  # -> 진짜 수업 못들음
    print(l_set)

    for i in r_set:  # 옷 빌려줄 수 있는 애들 중
        if i - 1 in l_set:  # 뒷번호가 진짜_수_못이면
            l_set.remove(i - 1)
        elif i + 1 in l_set:  # 앞번호가 진짜_수_못이면
            l_set.remove(i + 1)

    return n - len(l_set)