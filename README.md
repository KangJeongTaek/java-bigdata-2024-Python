# 빅데이터 언어 2024
빅데이터 자바 개발자 Python 학습 repository

## 1일차
- ### 파이썬 개발환경

    - [github](https://giyhub.com/) 가입

    - [git](https://get=scm.com/download/win) 설치

    - [githubdesktop](https://desktop.github.com/) 설치

    - [Python](https://python.org) 설치

    - [visualstudiocode](https://code.visualstudio.com/) 설치

    - [나눔고딕 코딩 글꼴](https://github.com/naver/nanumfont) 설치


- ### 파이썬 학습

     - #### 01 파이썬 개요

        - ##### 01-1 파이썬이란?
            - 1990년, 네덜란드계 귀도 반 로섬이 발표한 고급 프로그래밍 언어

        - ##### 01-2 파이썬의 특징
            - 인간다운 언어
            - 문법이 쉬워 빠르게 배울 수 있다
            - 무료이지만 강력하다
            - 간결하다
            - 프로그래밍을 즐기게 해 준다
            - 개발 속도가 빠르다

        - ##### 01-3 파이썬으로 할 수 있는 것
            - 웹 프로그래밍
            - 인공지능과 머신러닝
            - 수치 연산 프로그래밍과 데이터 분석
            - 데이터베이스 프로그래밍
            - 시스템 유틸리티 제작하기
            - GUI 프로그래밍
            - C/C++ 과 연결하기
            - 사물 인터넷
        
        - ##### 01-4 파이썬으로 할 수 없는 일
            - 시스템과 밀접한 프로그래밍 영역'
            - 모바일 프로그램 <- 현재는 가능


    - #### 02 파이썬 기초, 자료형
        
        - ##### 02-1 숫자형
            - 숫자 형태로 이루어진 자료형
                ```python
                123,345,0 # 정수
                123.45,-1234.5,3.4e1 0#실수
                0o34,0o25 #8진수
                0x2A, 0xFF #16진수
                ```
            - 사칙 연산
                ```python
                # 자바와 크게 다를 것 없지만, 나누기는 3가지로 분류된다.
                # '/' <- 정확하게 실수로 나누기
                # '//' <- 정수로만 나누기
                # '%' <- 정수로 나눈 나머지
                # '**' <- 제곱 연산
                ```

        - ##### 02-2 문자열 자료형
            - 파이썬에서 \n, \t 이외의 이스케이프 문자는 잘 사용되지 않는다.
            - 여러 줄 문장을 쓸 때
                ```python
                # """|| ''' || \n 가능
                ```
            - 문자열 연산
                ```python
                # +,*
                # +는 문자열을 합쳐서 하나의 문자열을 만듦
                # *는 문자열을 정수만큼 반복
                ```
            - 문자열 길이 구하기
                ```Python
                ## - len("문자열")
                ```
            - 문자열 인덱싱과 슬라이싱
                ```python
                # "문자열"[인덱스]
                # cp[8] = 'd'  잘못된 문법  # 문자열은 배열이긴 하나, 값을 변경할 수 없다
                # : 뒤에 있는 숫자는 항상 +1
                ```

            - 문자열 포매팅(format string)
                ```python
                ## 파이썬에서는 %d,%s,%c 등 포맷스트링용 연산자 사용 빈도가 낮다.
                ```
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
                    


        - ##### 02-3 리스트,튜플 자료형
            - 리스트 - 수정, 삭제 가능
            - 튜플 - 수정, 삭제 불가 그 외에는 리스트와 동일


        
## 2일차

- ### 파이썬 학습

    - #### 02 파이썬의 기초, 자료형
        - #### 02-4 딕셔너리, 집합
            - 딕셔너리 : 단어 그대로 '사전'이라는 뜻
            - Key와 Value를 한 쌍으로 가지는 자료형
                ```python
                {Key1: Value1,Key2:Value2,Key3:Value3, ...}

                dic = {'name':'pey','phone':010-9999-1234','birth':'1118}
                ```
            - 딕셔너리 출력 방법
                ```python
                print(dic['name'])
                ```
            - 딕셔너리 추가, 삭제
                ```python
                dic['home'] = 'Busan' # 값 추가
                del dic['name'] #값 삭제
                ```
            - 주의 사항
                - 키 값은 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시된다
                - 키값은 리스트로 쓸 수 없다. 그리고 되도록 문자로 사용하도록 하자

            - 딕셔너리 관련 함수
                - 딕셔너리에 현재 존재하는 키 목록
                    ```python
                    dic.keys()
                    ```
                - 딕셔너리의 Key,Value 한 쌍 얻기
                    ```python
                    dic.items()
                    ```
                -  딕셔너리 값 가져오기
                    ```python
                    dic.get('name')
                    ```
                - 딕셔너리 안에 키가 있는지 확인
                    ```python
                    'name' in dic
                    ```
                - 딕셔너리에 현재 존재하는 값 목록
                    ```python
                    dic.values()
                    ```
                - 딕셔너리에 현재 존재하는 값 삭제
                    ```python
                    dic.pop('name') # 삭제한 값 리턴

                    dic.clear() ## 데이터 삭제

                    del dic ## 완전 삭제
                    ```

            - 집합 : 중복을 허용하지 않으며 , 순서가 없다.
                ```python
                set([1,2,3,4,3,2,1]) = {1,2,3,4}
                ```
        - #### 02-5 불 자료형
            - 참 또는 거짓
                ```python
                a = True # T 대문자
                b = False # F 대문자
                ```
            - 값이 있는 자료형은 참이며 값이 없으면 거짓이다
                ```python
                print(bool(0)) #False
                print(bool(1)) #True
                print(bool(-1)) #True
                print(bool({1,2,3})) # True
                print(bool({})) #False
                print(bool('')) #False
                print(bool('H')) #True
                print(bool(None)) #False

                #빈값,None,0는 False 이 외의 값들은 True
                True + False #가능  <- 1나옴
                ```

        - #### 02-6 None형
            - None
                ```python
                c = None
                #c + 1  <- 불가능
                ```

        - #### 02-7 변수
            - 얕은 복사
                ```python
                a = [1,2,3]
                b = a #얕은 복사, 같은 주소값을 공유한다.
                print(id(a))
                print(id(b))
                del b[2]
                print(a) #a 안에 있는 3도 삭제 된다.
                ```
            - copy 모듈 이용하기(깊은 복사)
                ```python
                from copy import copy
                a = [1,2,3]
                b = a
                d = copy(a) #깊은 복사, 다른 주소값을 가진다.
                del d[2]
                print(a)
                ```
        - #### 02-8 제어문
            - if 문
                - 파이썬에서는 들여쓰기 항상 신경쓰기!
                ```python
                """indentation(들여쓰기) == space 4
                if 조건문 :
                   실행문_문장1
                   실행문_문장2
                    ...
                elif 조건문 :
                    실행문_문장1
                    ...
                else :
                   실행문_문장1
                    ...
                """
                ```

            - for 문
            - while 문

## 3일차

## 4일차

## 5일차

## 6일차

## 7일차

## 8일차

## 9일차
