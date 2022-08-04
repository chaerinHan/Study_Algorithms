## Programmers-Level2.Best Album
## https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=python3

def solution(genres, plays):
    ## 장르별로 가장 많이 재생된 노래 최대 두 개
    ## genres: {장르1, 장르2, 장르3...}, plays: {장르1 횟수, 장르2 횟수, 장르3 횟수...}
    ## 장르 (횟수,고유 번호)

    playsDict = {}  # { 장르: 총 재생 횟수 }
    genresDict = {}  # { 장르: [ ( 플레이횟수, 고유번호 ) ] }
    answer = []

    for i in range(len(genres)):
        if genres[i] in playsDict:
            playsDict[genres[i]] += plays[i]
        else:
            playsDict[genres[i]] = plays[i]

        if genres[i] in genresDict:
            genresDict[genres[i]].append([plays[i], i])  ## append([횟수, 고유번호])
        else:
            # [재생횟수, 고유번호]의 list형태로 추가
            genresDict[genres[i]] = [[plays[i], i]]

            # playsDict를 내림차순으로 정렬
    genre_rank = sorted(playsDict, key=playsDict.get, reverse=True)

    for x in genre_rank:
        # 재생횟수(내림차순), 고유번호(오름차순)으로 정렬해준다
        play_rank = sorted(genresDict[x], key=lambda x: (-x[0], x[1]))

        # 노래가 하나라면 하나만, 아니라면 두개 추가
        if len(play_rank) == 1:
            answer.append(play_rank[0][1])
        else:
            for i in range(2):
                answer.append(play_rank[i][1])

    return answer