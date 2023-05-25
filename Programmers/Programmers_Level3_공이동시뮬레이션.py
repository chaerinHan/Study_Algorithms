## Programmers_Level3_공이동시뮬레이션
## https://school.programmers.co.kr/learn/courses/30/lessons/154540
## 18.05.2023

def solution(n, m, x, y, queries):
    answer = -1
    # 쿼리를 역으로 만들기
    queries.reverse()

    sr, sc, er, ec = x, y, x, y

    for i, j in queries:  # 증가 -> 감소 로 감소 -> 증가로 계산하기
        # 좌 # 열 감소니깐 증가로
        if i == 0:
            if sc == 0:  # 시작 col 이 0인 경우
                ec = min(m - 1, ec + j)  # 끝 col의 범위를 제한 (맵 맨 끝 칸 증가한 값)

            else:  # 0이 아닌 경우
                if sc + j >= m:  # 격자 벗어나는 경우
                    return 0  # 종료
                sc = min(m - 1, sc + j)  # 끝으로 가는 값, 증가한 값 비교
                ec = min(m - 1, ec + j)

        elif i == 1:  # 우 # 열 증가니깐 감소로
            if ec == m - 1:  # 끝 col이 m-1 (맵 맨 끝)
                sc = max(0, sc - j)
            else:
                if ec - j < 0:  # 끝 col을 좌측으로 j만큼 감소한 결과가 0보다 작으면 맵 아웃
                    return 0
                sc = max(0, sc - j)
                ec = max(0, sc - j)

        elif i == 2:
            # 행 감소니깐 증가로
            if sr == 0:
                er = min(n - 1, er + j)
            else:
                if sr + j >= n:  # sr(시작row)를 밑으로 j만큼 이동한 결과 >= n 이면 목표지점 갈 수 X
                    return 0
                sr = min(n - 1, sr + j)
                er = min(n - 1, er + j)
        else:  # i == 3
            # 행 증가니깐 감소로
            if er == n - 1:
                sr = max(0, sr - j)
            else:
                if er + j < 0: return 0  # 위로 j만큼 이동해서 0보다 작으면 갈 수 X

                sr = max(0, sr - j)
                er = max(0, er - j)

    return ((er - sr) + 1) * ((ec - sc) + 1)