'''
# 문자열 형식화(format)

for i in range(1, 11):
    print(f'1/{i} = {1/i}') # 초창기부터 쓰던 formant 형식
    # {}안에는 결과값이 나옴

for i in range(1, 11):
    print(f'1/{i:2d} = {1/i:6.3f}')
    # i:2d -> d는 10진수로 출력 2d는 최소2자리를 잡아서 10진수 출력
    # 두 자리의 여유를 가지고 출력한다는 뜻
    # i:6.3f -> f는 float 6.3f는 최소6자리를 잡아서 소숫점은 3자리 까지 출력

print('\n')

i = 123
print(f'1/{i:2d} = {1234567.123456:6.3f}')

print('\n')

print('{}/{} = {}'.format(2, 4, 2/4))

print('\n')

print('{0}/{1} = {2} {0} {1}'.format(2, 4, 2/4))

print('\n')

print('{:2d}/{:2d} = {:5.2f}'.format(2, 3, 2/3))

print('\n')

# 굳이 d, f 처럼 형식 안잡아줘도 알아서 처리하긴함

print('{:2d}/{:2d} = {:5.2e}'.format(2, 3, 2/3))

print('\n')

# e는 지수승 처리

print(f'1/{i:2d} = {1/i:6.3f}')
print('1/{:2d} = {:6.3f}'.format(i, 1/i))
# 위 두개는 같은표현

print('\n')

print('{0:<2} / {1:<2} = {2:<5}'.format(2, 4, 2/4))
# 기본적으로 오른쪽정렬하기때문에 이렇게 왼쪽정렬도가능

print('\n')
      
print('{:02}/{:02} = {:5.2e}'.format(2, 3, 2/3))
# 이거는 빈자리를 공백이아닌 0을채움

print('\n')

print('10진수 {0:d} = 8진수 {0:o} = 16진수 {0:x}'.format(160))

print('\n')

print('{:,}'.format(650000000))
# 큰 숫자에 자동으로 , 넣어 보기 편하게 해줌

print('\n')

# 이름으로 양식 채우기

print("제 이름은 {fname}이구요, 고향은 {hometown}입니다.".format(fname='홍길동', hometown='파주'))

# 마치 {}를 key value처럼 사용

# 보통 template 만들어서 쓰기도함

template = '''
'''
안녕하세요 {phone} {name} 고객님,

이번 달 납부하실 금액은 총 {total_price}원 입니다.
납기일은 {due_date} 입니다.

주소 : {address}
연락처 : {phone}

고객센터: 080-000-0000
'''
'''

msg = template.format(phone='010-1234-5678', name='홍길동', total_price=38000, due_date='2021.05.21', address='경기도 파주시')

print(msg)

print('\n')

# 위에는 일일히 데이터 입력해야되니 dictionary 사용하면 편함

info = {'phone': '010-1234-5678', 'name': '홍길동', 'total_price': 38000, 'due_date': '2021.05.21', 'address': '경기도 파주시'}

msg1 = template.format(**info)
print(msg1)

# **은 keyword 인수로 key에 해당하는 value를 전달



# 리스트에 결과 저장

# 연산 결과 모으기

L = []
for i in range(1, 11):
    L.append(1/i)
L


# 리스트 내장
L = []
for i in range(10) :
    L.append(i*i)

L = [i*i for i in range(10)]

sum([1/(i*i) for i in range(1, 101)])

# 문자열의 리스트를 한번에 모두 대문자로 만들기
L = ['Alice', 'was', 'beginning', 'to', 'get', '...']
[w.upper() for w in L]

# if문하고도 같이 사용 가능
[line.strip() for line in open('data/sample/log') if 'gslee' in line]

# open은 기본모드로 읽기고 line 단위로 파일을 읽어옴, 
# ( line in open('data/sample/log') ) 파일의 각 line에 대해서 'gslee'이 line에 포함될 경우 출
# strip()은 좌우 공백, 널문자 제거

# 길이가 0인 문자열 혹은 공백만 포함하는 문자열을 제외한 리스트를 만드는 예
L = ['Alice', '', 'was', ' ', 'beginning', 'to', 'get', '']
[w for w in L if w.strip()]
# '' -> False, ' ' -> True, 따라서 위에서는 길이 0인 문자 제거

s = '기온(ºC)'
[c for c in s if '가' <= c <= '힣'] # 한글만 모음, ['기', '온']

# join()과 ''(문자열을 붙이는 문자열 paste string)
''.join([c for c in s if '가' <= c <= '힣']) # ''를 사용하여 요소 붙임, '기온'
':'.join([c for c in s if '가' <= c <= '힣']) # ':'를 사용하여 요소 붙임, '기:온'


# 한글만 모으는 함수
def hangulOnly(s):
    return ''.join([c for c in s if '가' <= c <= '힣'])

names = ['기온(ºC)', '강수량(mm)']
[hangulOnly(name) for name in names] # ['기온', '강수량']
'''

# 연산 결과 시각화_Matplotlib(그래프 그리기)

import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [10, 15, 30]) # 1, 2, 3은 x값 10, 15, 30은 y값
plt.grid() # 격자추가
plt.show()

# 2차 함수 그래프 그리기
xs = list(range(-10, 11))
ys = []
for x in xs:
    y = 2*x*x - 5*x + 8
    ys.append(y)
plt.plot(xs, ys)
plt.grid()
plt.show()

import numpy as np # numpy는 벡터연산이가능 요소끼리 빠르게 곱이가능

x = np.arange(-10, 10, 0.1) # 실수도 가능, 더 매끈하게 그래프를 그림
y = 2*x*x - 5*x + 8 # 배열 형태가 편한 이유, 각 요소에 각각 곱함, 수치연산에서 numpy의 장점이 드러남, for사용 x

plt.plot(x, y)
plt.grid()
plt.show()

# Sin함수, degree 단위
import math

xs = []
ys = []
for degree in range(0, 360+1, 10):
    rad = math.radians(degree) # radian 변환
    y = math.sin(rad)
    xs.append(degree)
    ys.append(y)
plt.plot(xs, ys)
plt.grid()
plt.title('Sine graph') # 제목 추가
plt.show()

# Sin그래프. radian 단위, numpy 활용, math의 sin은 값을 하나씩 넣을 수 있지만, numpy의 sin은 벡터연산 가능

x = np.linspace(0, np.pi*2, 100) # 0~ 2pi까지 100개의 간격으로 점을 만들어라
y = np.sin(x)

plt.plot(x, y)
plt.grid()
plt.show()

# 수치연산시 그냥 numpy를 활용하자

# 이번엔 sin, cos 동시에 그리기, degree 단위

xs = []
ys1 = []
ys2 = []
for degree in range(0, 360+1, 10):
    rad = math.radians(degree)
    xs.append(degree)
    ys1.append(math.sin(rad))
    ys2.append(math.cos(rad))
plt.plot(xs, ys1, c='green') # color 옵션도 줄 수 있음
plt.plot(xs, ys2, c='red')
plt.grid()
plt.show()

# sin, cos 동시에 그리기, radian 단위, numpy 활용

x = np.linspace(0, np.pi*2, 100)
y1 = np.sin(x)
y2 = np.cos(x)

'''
x = np.linspace(0, 360, 100)
r = np.radians(x) # degree는 이렇게 radian 변환만 해주면 
y1 = np.sin(r)
y2 = np.cos(r)
'''

plt.plot(x, y1, c='green')
plt.plot(x, y2, c='red')
plt.grid()
plt.show()

# sin(x) + 0.9sin(2x)의 그래프를 (0<=x<=6pi)

x = np.linspace(0, np.pi*6, 100)
y = np.sin(x) + 0.9*np.sin(2*x)
plt.plot(x, y)
plt.grid()
plt.show()

# 급수 그래프, 누적 될 때마다 값이 어떻게 되는지

xs = []
ys = []
acc = 0.0
for x in range(1, 101):
    acc += 1/pow(x, 2)
    xs.append(x)
    ys.append(acc)
plt.plot(xs, ys)
plt.grid()
plt.show() # 실제 1.6449340668482264에 근접함을 눈으로 볼 수 있다.

# 표준 모듈 itertools
from itertools import accumulate

y = 1 / pow(np.array(xs), 2)
print(list(accumulate(y))) # 위에서 for문으로 누적한거 쉽게 가능

# 이제 급수 그래프 쉽게 코딩 가
x = np.arange(1, 101)
y = 1 / pow(np.array(xs), 2)
acc = list(accumulate(y))
plt.plot(x, y, c='red')
plt.plot(x, acc, c='green')
plt.grid()
plt.show()

# 요약하면 수치 연산은 numpy를 활용한다.
