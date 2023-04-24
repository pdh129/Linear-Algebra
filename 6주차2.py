# for문

# 복리 계산

for i in range(10):
    print(i+1, 100*pow(1.03, i+1))

print('\n')

for i in range(1, 11):
    print(i, 100*pow(1.03, i))

print('\n')
    
for i in range(1, 21, 2):
    print(i, 100*pow(1.03, i)) # 홀수년도

print('\n')

for i in range(2, 21, 2):
    print(i, 100*pow(1.03, i)) # 짝수년도


print('\n')


# y=x^2

for x in range(-5, 6, 1):
    y= pow(x, 2)
    print('x=', x, 'y=', y)

print('\n')
 

'''
for x in range(-5, 6, 0.5):
    y= pow(x, 2)
    print('x=', x, 'y=', y) # TypeError 뜸 range에서는 정수만 들어감, 실수는 불가
'''

for x1 in range(-5, 6, 1): # 트릭을 이용한 실수 처리법
    x = x1 / 10
    y= pow(x, 2)
    print('x=', x, 'y=', y)

print('\n')

# 실수 처리 위한 모듈 numpy -> 수치 연산용
import numpy as np # 보통 np로 줄여서 씀

n1 = np.arange(0, 1.0, 0.1) # range랑 같음
# np.arrange는 리스트가 아닌 배열(array)을 만듬
# 리스트는 어떠한 자료형이라도 묶을 수 있지만
# 배열은 같은 자료형만 묶을 수 있음
# 즉, 위는 실수형 자료형만 묶음
print(n1)
print(type(n1))

print('\n')

# y=x^2

for x in np.arange(-5, 6, 0.5):
    y = x ** 2
    print('x=', x, 'y=', y)

print('\n')

n2 = np.linspace(0, 10, 13)
print(n2)

print('\n')

# array와 차이점은 여기는 0과 10은 반드시 포함하면서 0~10을
# 13등분한 배열(array)를 만듬
# 가끔 수치연산 하다 끝값이 포함된 연산을 할경우 linearspaec인 linspace 사용
# 마찬가지로 for문에 사용 가능


# for문의 수학적인 활용 (수열과 급수 연산

# 수열
for i in range(1, 11):
    print('1/', i, '=', 1/i) # 수열 출력

print('\n')

for i in range(1, 11):
    print('1/(', i, '**2)', '=', 1/(i**2), sep='') # 기본적으로 ,를 기준으로 띄어쓰기하여 출력
    # 위는 ,의 공백없이 출력
    # 기본적으로 print('1', i, '**2', '=', 1/(i**2), sep=' ')로 되어있음

print('\n')

sign = 1
for i in range(1, 11):
    print('{0}{1}/({2}**2)='.format('+' if sign == 1 else '-', 1, i), sign * 1/(i**2), sep='')
    sign = -sign
# 참고로 대괄호 안에 0 1 2는 생략가

print('\n')

# 누적

acc1 = 0
for i in range(1, 1001):
    acc1 = acc1 + i # 또는 acc1 += 1 (확장치환문)
print(acc1)

print('\n')

acc2 = 0.0
for i in range(1, 1001):
    acc2 += 1/i # 역수 누적
print(acc2)

print('\n')

# 리만 제타함수 등식 성립하는지 확인하기

acc3 = 0.0
for i in range(1, 1001):
    acc3 += 1/(i ** 2) # 역수 제곱 누적
print(acc3)

print('\n')

import math
acc4 = pow(math.pi, 2) / 6
print(acc4) # 위의 acc3과 거의 근사한 값임을 확인할 수 있음

print('\n')

print(acc4 - acc3) # 오차 확인

print('\n')

sign = 1
acc5 = 0.0
for i in range(1, 1001):
    acc5 += sign * 1/(i ** 2) # 역수 제곱 부호 바뀌면서 누
    sign = -sign
print(acc5)

print('\n')

# if문과 함께 for문 사용하기 (DATA의 필터역할을 하여 처리)
scores = [50, 30, 95, 70, 90]
for score in scores:
    if score >= 90:
        print(score, 'A')

print('\n')

import random # 난수 사용
scores = []
for i in range(200):
    scores.append(random.randint(0, 100))

count = 0
for score in scores:
    if score >= 90:
        count +=1
print(count) # 90점 넘는 애들 수 출력

print('\n')

count1 = 0
count2 = 0
for score in scores:
    if score >= 90:
        count1 +=1
    else:
        count2 += 1
print(count1, count2) # 90점 넘는 애들과 아닌애들 수 출력

print('\n')

s = 'HIV는 complex retrovirus 로 여러 가지 효소를 virion 내에 포함하고 있기 때문에 단순히 cDNA를 transfaction 해서는 감염이 되지 않는다.'
eng = '' # 빈 문자열 생성
for c in s:
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z': # c가 영어 소문자 or 대문자만 빼내는 일반적인 방법
        eng += c
    else:
        eng += ' ' # 영어 소문자 or 대문자가 아니면 공백처

print(eng)
print('\n')





