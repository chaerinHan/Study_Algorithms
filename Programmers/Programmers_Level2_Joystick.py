## Programmers_Level2_Joystick
## https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3
## 10.26.2022

def solution(name):
    # 생각할 것 1. 오름차순 or 내림차순이 빠른지
    # 2. A가 연속해서 있는지
    # 상하 cnt + 좌우 cnt
    answer = 0
    minMove = len(name) - 1  # 1. 최소 움직임
    next = 0

    for i, char in enumerate(name):
        # i는 인덱스 char은 글자
        # 2. 오름차순 or 내림차순이 더 빠른지
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1  # 현재 알파벳 다음 알파벳 인덱스
        # 3.지금 알파벳부터 연속된 A있는지 찾기
        while next < len(name) and name[next] == 'A':
            next += 1  # 현재 위치 다음의 A 위치

        # ** 한 방향으로만 or 좌우 왔다갔다 하는게 더 빠른지 확인해아함
        # minMove = min(minMove, i + i + len(name) - next)
        # 기존 방법, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교
        minMove = min([minMove, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    answer += minMove
    return answer


print(solution("AAAABABAAAA"))