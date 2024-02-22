# 빅데이터 언어 2024
빅데이터 자바 개발자 Python 학습 repository

## 1일차
- 파이썬 개발환경

    - [github](https://giyhub.com/) 가입

    - [git](https://get=scm.com/download/win) 설치

    - [githubdesktop](https://desktop.github.com/) 설치

    - [Python](https://python.org) 설치

    - [visualstudiocode](https://code.visualstudio.com/) 설치

    - [나눔고딕 코딩 글꼴](https://github.com/naver/nanumfont) 설치


- 파이썬 학습

     - 01 파이썬 개요

        - 01-1 파이썬이란?
            - 1990년, 네덜란드계 귀도 반 로섬이 발표한 고급 프로그래밍 언어

        - 01-2 파이썬의 특징
            - 인간다운 언어
            - 문법이 쉬워 빠르게 배울 수 있다
            - 무료이지만 강력하다
            - 간결하다
            - 프로그래밍을 즐기게 해 준다
            - 개발 속도가 빠르다

        - 01-3 파이썬으로 할 수 있는 것
            - 웹 프로그래밍
            - 인공지능과 머신러닝
            - 수치 연산 프로그래밍과 데이터 분석
            - 데이터베이스 프로그래밍
            - 시스템 유틸리티 제작하기
            - GUI 프로그래밍
            - C/C++ 과 연결하기
            - 사물 인터넷
        
        - 01-4 파이썬으로 할 수 없는 일
            - 시스템과 밀접한 프로그래밍 영역'
            - 모바일 프로그램이 <- 현재는 가능


    - 02 파이썬 기초, 자료형
        
        - 02-1 숫자형
            - 숫자 형태로 이루어진 자료형
                - 정수 ex) 123,345,0
                - 실수 ex) 123.45,-1234.5,3.4e10
                - 8진수 ex) 0o34,0o25
                - 16진수 ex) 0x2A, 0xFF

            - 사칙 연산
                - 크게 다를 것 없지만, 나누기는 3가지로 분류된다.
                - / <- 정확하게 실수로 나누기
                - // <- 정수로만 나누기
                - % <- 정수로 나눈 나머지
                -  ** <- 제곱 연산

        - 02-2 문자열 자료형

            - 파이썬에서 \n, \t 이외의 이스케이프 문자는 잘 사용되지 않는다.
            - 여러 줄 문장을 쓸 때 """,''' \n
            - 문자열 연산은 +,* /+는 문자열을 합쳐서 하나의 문자열요 만듦 / *는 문자열을 몇 번 반복

            - 문자열 길이 구하기
                - len("문자열")

            - 문자열 인덱싱과 슬라이싱
                "문자열"[인덱스]
                cp[8] = 'd'  X  # 문자열은 배열이긴 하나, 값을 변경할 수 없다
                : 뒤에 있는 숫자는 항상 +1

            - 문자열 포매팅(format string)
                파이썬에서는 %d,%s,%c 등 포맷스티링용 연산자 사용 빈도가 낮다.

            - format 함수로 포맷팅(가장 일반적)
                ```Python
                ## 날짜를 포맷으로 만들 때
                month = 2
                day = 21
                hour = 15
                mins = 18
                print('오늘은 {0:02d}월 {1:02d}일 {2:02d}시 {3:02d}분입니다.'.format(month,day,hour,mins))

                income = 6000000 # 육백만원

                print('이번 달 매출액은 {0:,d}원 입니다.'.format(income))

                PI = 3.1415926536
                print('파이는{0:.2f}'.format(PI))
                print('{0:f}'.format(PI)) #실수형은 d(정수형 포맷팅) 불가
                ```

            - f문자열 포매팅
                ```Python
                name = '홍길동'
                age = 30
                print(f'나의 이름은{name}입니다. 나이는 {age}입니다.')
                ```

            - 문자열 관련 함수들
                ```Python
                a = 'Life is too short, You need Python'
                print(a.count('Life'))
                print(a.count('o')) # 문자열 중 o의 개수
                print(a.find('sh')) #문자가 처음 나온 위치 < 찾지 못 하면 -1 반환
                print(a.index('t')) #첫번째 t의 위치 < 찾지 못 하면 오류 #index()는 count()로 갯수가 0이 아닐 때만 호출]
                print(','.join('abcde')) #문자열 abcde 사이에 ','를 삽입
                print(a.upper()) #대문자 만들기
                print(a.lower()) #소문자 만들기
                print(a.capitalize()) #제일 첫번째 글자만 대문자로 만들기
                
                origin = '      Hi        '
                print(f'++{origin}++')
                print(f'++{origin.lstrip()}++')
                print(f'++{origin.rstrip()}++')
                print(f'++{origin.strip()}++')
              
                 print(cp.replace('too','').replace(' short','long'))
                # cp.split(' ') 공백을 기준으로 문자열을 잘라 배열로 반환
                ```
                    


        02 -3 리스트 자료형


        
## 2일차

### 파이썬 학습

    - 파이썬 기초문법
        - 딕셔너리. 집합
        - 불형
        - None형
        - 제어문

## 3일차

## 4일차

## 5일차

## 6일차

## 7일차

## 8일차

## 9일차
