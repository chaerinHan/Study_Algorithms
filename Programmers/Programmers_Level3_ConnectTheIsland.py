## Programmers_Level3_Connect the island
## https://school.programmers.co.kr/learn/courses/30/lessons/42861?language=python3
## 11.02.2022

def solution(n, costs):
    answer = 0
    # 1 비용 먼저 정렬, 오름차순 정렬
    costs.sort(key=lambda x: x[2])  # 인덱스 2가 비용

    # 2 집합 만들기 -> 방문을 확인하는 리스트에 가장 cost가 작은 섬 넣어주기
    visit = [costs[0][0]]

    while len(visit) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in visit) and (cost[1] in visit):  # 연결되어있으니깐
                continue
            if (cost[0] in visit) or (cost[1] in visit):  # 연결안되었다는거
                answer += cost[2]
                visit.append(cost[0])
                visit.append(cost[1])
                visit = list(set(visit))
                costs.pop(i)  # 다 했으니깐 빼버리기
                break
    return answer