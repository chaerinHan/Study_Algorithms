## Programmers-Level1.Digit List
## https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3
## 07.26.2022

# [프로그래머스 - 전화번호 목록]

def solution(phone_book):

    phone_book.sort() ## phone_book 정렬

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1): # startswith: 문자열이 특정 문자열로 시작하는지 여부 알려주는 함수
            return False
    return True