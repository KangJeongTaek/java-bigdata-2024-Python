# file : p28_debugging.py
# desc : 디버깅 학습, 예외처리 추가

class newCalc:
    def add(self,a,b):
        res = a+b
        return res
    def minus(self,a,b):
        res = a-b
        return res
    def multi(self,a,b):
        res = a*b
        return res
    def div(self,a,b):
        try:
            res = a/b
        except:
            print('제수에 0을 넣으면 안됩니다.')
            res = 0
        return res
    
while True:
    try:
        select = int(input('메뉴 : 1. 더하기 2. 빼기 3. 곱하기 4. 나누기 >>'))
    except Exception as e:
        print('제대로 된 숫자를 입력해주세요.')
        input()
        continue
    if select == 1:
        try:
            x,y = map(int,input('두 수를 입력(정수) > ').split())
        except:
            print('정수만 입력하세요')
            input()
            continue
        calc = newCalc()
        print(f'더하기 결과  {x} + {y} = {calc.add(x,y)}')
    elif select == 2:
        try:
            x,y = map(int,input('두 수를 입력(정수) > ').split())
        except:
            print('정수만 입력하세요')
            input()
            continue
        calc = newCalc()
        print(f'빼기 결과  {x} - {y} = {calc.minus(x,y)}')
    elif select == 3:
        try:
            x,y = map(int,input('두 수를 입력(정수) > ').split())
        except:
            print('정수만 입력하세요')
            input()
            continue
        calc = newCalc()
        print(f'곱하기 결과  {x} × {y} = {calc.multi(x,y)}')
    elif select == 4:
        try:
            x,y = map(int,input('두 수를 입력(정수) > ').split())
        except:
            print('정수만 입력하세요')
            input()
            continue
        # if y ==0:
        #     print('제수에 0을 입력하지 마시오.')
        #     input()
        #     continue
        calc = newCalc()
        print(f'나누기 결과  {x} ÷ {y} = {calc.div(x,y)}')
    elif select == 5:
        print('프로그램을 종료합니다')
        input()
        break
    else:
        continue
