## Programmers-Level2.Trucks On Bridge
## https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python
## 08.11.2022

def solution(bridge_length, weight, truck_weights):
    # bridge_length: 다리에 올라 갈 수 있는 트럭 수
    # weight: 다리가 견딜 수 있는 무게
    # truck_weights: 트럭별 무게

    bridge = [0 for _ in range(bridge_length)]  # 다리 길이만큼 리스트 생성
    print("bridge:", bridge)
    time = 0  # 모든 트럭 건너려면 최소 몇초

    while len(bridge):
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time

