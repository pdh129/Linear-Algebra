a, b = 10, 20

'''
print(a/b) # ZeroDivisionError, 예외처리 필요
'''

'''
open('a.txt') #FileNotFoundError
'''

try: # try했는데 에러날시 except로 대처함
    a/b
    open('a.txt')  # a/b가 가능하면 open으로 넘어와서 에러봄, a/b가 불가능하면 여기실행x
    print('here1') # open도 에러가없으면 여기 실행
except ZeroDivisionError:
    print('...')
except FileNotFoundError:
    print('file does not exist')
except (TypeError, NameError): # 튜플이 조건으로 들어옴, 에러 두개를 동시에 처리 TypeError or NameError
    print('here2')
else:
    print('ok') # try에서 모두 에러가 없으면 else 출력
finally:
    print('done') # 예외가 발생하든, 안하든 얘는 무조건 마지막에 출력

# except를 통째로 쓰면 try에 모든 error를 예외처리
# except 옆에 조건쓰면 그거에 해당하는 에러만 예외처리

''' try ~ except를 안쓰고 예외처리 하는 방법 
import os
fname = 'nofile.txt'
if os.path.exists(fname):
    open(fname)
else:
    print('[ERROR]')
'''

''' try ~ exept 사용하여 예외처리
import os
try:
    fname = 'nofile.txt'
    open(fname)
except FileNotFoundError:
    print('[ERROR]')
'''

# 둘의 차이점은 if else는 미리 사전에 Error인지 확인후 실행결정
# try ~ exept는 일단 실행하고 문제가 생기면 에러 출력하여 나중에 수정하라

# if else보다 try except가 코딩 보기에 더좋음
# try except는 일단, 정상처리 다하고 마지막에 예외처리 몰아서함
# if else는 각 문단마다 예외처리


class A:
    pass
print(type(A)) # 결과 type으로 나옴
print(type(FileNotFoundError)) # 결과 type으로 나옴 즉, class라는뜻

A()
FileNotFoundError() # class이기 때문에 이렇게 사용가능, 계층관계에있음, 이 아래에 Error가 여러개 속해있음
# 서로 부모-자식관계로 상속관계

# zerodivision, floatingpoint, overflow는 같은 부모 class인 ArithmeticError에서 상속받음

print(issubclass(ZeroDivisionError, ArithmeticError)) # ZeroDivisionError가 ArithmeticError의 서브 class인지확인하는 것
# 결과로 True 나옴, 즉, ArithmeticError한테 상속받음

print(issubclass(ArithmeticError, Exception)) # True

print(issubclass(Exception, BaseException)) # True

# 즉, 다음과 같은 상속관계
# BaseException -> Exception -> ArithmeticError -> Zero, floating, overflow Error
# 만일, Exception Error를 예외처리하면 그아래에있는 하위 Error는 모두 포함해서 처리
'''
try: ~
except Exception:
    print('...')
'''


# 내가 원하는 예외처리 정의도가능
# 사용자 정의 에러

class BadUserNameError(LookupError): # LookupError에서 상속받은 내가만든 에러
    pass

issubclass(BadUserNameError, LookupError) # True

try:
    ... # pass라고 해도됨 그냥 자리채우기용
    raise BadUserNameError
except BadUserNameError:
    print('....')

def checkUserName(uname):
    ...
    if True:
        raise BadUserNameError # raise는 사용자가 강제로 예외발생시키는것
    return uname

checkUserName('gslee') # 결과로 BadUserNameError 나옴.





for i in range(10): # 0~9
    print(i)

for i in range(3, 10): # 3~9
    print(i)

for i in range(3, 10, 1): # 3~9 1씩 증가 (default로 1)
    print(i)

for i in range(3, 10, 2): # 3~9 2씩 증가
    print(i)
