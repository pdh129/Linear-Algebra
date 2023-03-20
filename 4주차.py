import math
import sys
import os
from math import pi, e # math 모듈로부터 pi, e 이름을 쓰겠다. math생략가능
from math import * # math에 모듈에있는거 다씀.
import random as r # 랜덤수 발생시키는 모듈의 이름을 random치기 귀찮으니 r로 바꿈
import cmath # 복소수 영역 사용

#math
print(math.pi)
print(math.e)
print(math.sin(math.pi)) # 1.224e-16, pi가 부정확해서 오차에의해 0에 가까운값이 나옴
print(math.sin(math.pi*2)) # -2.449e-16

#sys
print(sys.version) # 파이썬 버전 3.9.13
print(sys.version_info.major) # 3, 파이썬 버전 3

#os
print(os.getcwd()) # 현재 작업중인 디렉토리
print(os.path.getsize(r'C:\Users\kw\Desktop'))

#from import
print(pi)
print(e)

print(sin(1))

print(sqrt(2))
print(pow(2,0.5))
print(2**0.5)

#import random as r
print(r.random())

#cmath
#print(math.sqrt(-2)) # 오류남
print(cmath.sqrt(-2), '\n \n')

#리스트
L = [1, 2, 'hello'] # 임의의 object를 모아둔 임의의 자료형 (수정이가능)(문자열은안됨)
# 배열과 비슷하지만(같은 자료형을 모아둔것) 전혀 다름
print(L[0])

L[0]=100
print(L)

del L[2] # 삭제
print(L)

L.append(3) # 리스트 맨오른쪽에 값 추가
print(L)
L.append(4)
print(L)

L.insert(0, 200) # 0번 index에 200 을 넣음
print(L)
L.insert(2, 1)
print(L)

L.extend([10, 20, 30]) # 리스트를 맨오른쪽에 추가
print(L)

L.reverse() # 리스트 순서가 뒤집힘
print(L)

L.sort() # 리스트 오름차순 정렬
print(L)

L.sort(reverse=True) # 리스트 내림차순 정렬  defualt가 False
print(L)

print(L.pop()) # 맨오른쪽에 데이터를 빼서 return
print(L)

print(L.pop(0)) # 0 index 값 빼서 return
print(L, '\n \n')

#튜플
t = (1, 2, 3) # 리스트랑 똑같지만 변경, 수정이안됨
#t[0] = 100 # 오류남

pl = [('one', 1), ('two', 2)] #리스트지만 튜플을 원소로 가짐
print(type(pl))
print(type(pl[0]))

#패킹과 언패킹
print(pl) # 데이터 2개 가짐
print(pl[0])

a,b = pl #  언패킹
print(a)
print(b)

def f(a, b):
    return a+b, a-b # 튜플로 패킹해서 값 반환

print(f(2, 3))

x, y = f(2, 3) # 언패킹
print(x)
print(y, '\n\n')

#사전 딕셔너리
#리스트랑 튜플은 접근할 때 index로 접근함, 순서가 있다는 의미, 즉, sequence 자료형을 뜻함
#사전은 index로 접근하지않음, 순서가 없다는 의미, key로 접근

member = {'basketball': 5, 'soccer' : 11, 'baseball' : 9}
#두개씩 짝지은건 왼쪽값을 key 오른쪽값을 value 두개를 합쳐서 value로 부름.
print(member['soccer']) # key를주면 그에 대응하는 value가 나옴
print(member) # 파이썬 업그레이드 되면서 그래도 입력한 순서대로 출력해줌
#key를 입력해서 주소를 찾아 value를 찾는거를 해쉬라함, 해쉬란 문자를 입력으로 넣는 함수
#key를 해쉬코드라 하고 그 결과가 value

#사전은 변경가능
member['soccer'] = 15
print(member)
member['volleyball'] = 6 # 추가
print(member)
del member['volleyball'] # 삭제
print(member, '\n\n')
#사전은 순서가 없기때문에 순서바꾸는 연산은 없음

#사전과 리스트,튜플 호환
print(member.keys())
q = list(member.keys()) # 사전의 key를 리스트로 바꿔 받음
print(q)
w = list(member.values()) # 사전의 value를 리스트로 바꿔 받음
print(w)
e = list(member.items()) # 사전의 item을 리스트로 바꿔 받음
print(e, '\n\n') # key:value는 튜플로 묶여서 리스트의 원소가 됨

#리스트를 사전으로 만듬
print(type(member)) # dict 자료형
r = dict(e) # 다시 리스트를 사전으로 만듬
print(r)
rq = dict(pl)
print(pl,'\n\n')

#key, value 합치기
ks = ('one', 'two', 'three')
vs = (1, 2, 3)
print(dict(zip(ks, vs))) # zip(key, value)
print(zip(ks, vs))
print(list(zip(ks, vs)))

#집합 자료형
sl = {1, 2, 3} # 사전과 같이 {} 쓰지만 key value 없으므로 set자료형이됨
print(sl)
print(type(sl)) # 집합자료형 특징 : 자료가 중복이 안됨, 순서도 의미 없음, 원소가 맞냐 아니냐만 따짐
sw = {1, 2, 3, 1, 2, 3}
print(sw)

se = 'I love python I love coffee'
print(se)
sr = se.split() # 문장을 쪼개서 리스트로 만듬
print(sr)
st = set(sr) # 리스를 집합으로 바꿈
print(st) # 문장에서 쓰인 단어만 중복없애서 들어감
print(len(st)) # 문장에 쓰인 단어 수 확인
sy = list(st) # 집합을 다시 리스트로 바꿈
print(sy)
