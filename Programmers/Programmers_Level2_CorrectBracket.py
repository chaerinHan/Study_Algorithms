## Programmers-Level2.Correct Bracket
## https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=python3
## 08.17.2022

def solution(s):
    answer = True
    result = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # (로 시작하는데 )가 안오면 false

    for i in s:
        if i == "(":
            result.append(i)  # ( 이면 stack에 추가
        else:  # i = )
            if result == []:  # result 비어있다는 건 지금 ) 로만 나왔다는것
                return False
            else:
                result.pop()

    return result == []