print('Hello')
print(2+3)
name = input('Name? ')
print('Hi', name)
print(5/2) # 2.5
print(5//2) # 2
print(5%2) # 1
print(2**3) # 8
pow(2,128) # 340282366...
pow(2.0,128) # 3.4028 e+38
#둘이 값은 같음 위는 int(엄청큼)형, 아래는 float(8byte)형
pow(2,1024) # 잘나옴
pow(2.0,1024) # overflow 에러
0.1 # 0.1
0.1+0.1 # 0.2
0.1+0.1+0.1 # 0.30000000000000004
# 이진수 0.1 = 십진수 2^-1, 0.01 = 2^-2, 0.001= 2^-3... 2로나눠짐
# 이진수 1 = 십진수 2^1
# 십진수 0.75 = 이진수 0.11
# 이진수의 2로나눠진값들의 조합으로 십진수만들어야함
# 십진수 0.1 = 이진수 ? 만들수X 순환소수됨
# 따라서, 무한소수됨. 8byte 넘으면 에러숫자남김 4.
# float 문제점 : 진법변환의 문제가있고, 유효자리수 존재(8byte), 에러를 가지고 있음
3+4j #(3+4j) : 복소수 표현
2>3 # False
2<3 # True
2+3 == 5 # True
2>=3
2<=3
2+3 ==
2+3 != 5
2.0 # 2.0
2. # 2.0
2e1 # 20.0
2.0e-1 # 0.2
ord('가') # 44032 (문자의 유니코드값 확인)
chr(44032) # '가' (코드로 문자 반환)
s='python'
s # 'python', ' " 상관 x
s+s # 'pythonpython' 문자연결
s*3 # 'pythonpythonpython' 문자반복
s[0] # 'p' 인덱싱
s[1] # 'y'
s[5] # 'n'
s[-1] # 'n'
s[1:3] # 'yt' 슬라이싱
s[1:30] # 'ython'
s[:3] # 'pyt'
s[1:] # 'ython'
s[:] # 'python'
s[:-1] # 'pytho' 
s[::2] # 'pto' 처음부터 끝까지 간격 2로, s[start:stop:stack], stack 안쓰면 기본값 1
s[::-1] # 'nohtyp' 문자열 뒤집기
print('-'*40) # ------------------------------------------------------------
len(s) # 6 길이구하는 함수
'th' in s # True th가 s안에 있는지?, 멤버쉽 테스트
L=[1, 2, 3, 4, 5] # List 자료형
type(L) # <class 'list'>
L # [1, 2, 3, 4, 5]
L[0] # 1
L[1:3] # [2, 3]
L+L # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
L*3 # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
len(L) # 5
3 in L # True
s # python
s[0] = 'p' # 오류남, 문자열 객체는 assignment 연산(대입)이 사용불가능함, 즉 문자열은 변경불가능
L[0] = 100 # List형은 가능
'P' + s[1:] # 'Python'
s.capitalize() # 'Python', 함수라고 안부르고 method라함, s라는 문자열 객체에 capitalize라는 함수가 속해있음
# 객체지향 프로그래밍이기 때문, 정수 실수 문자열 다 객체
# ctrl+space : 객체내 method 알려줌
s.upper() # 'PYTHON'
#s는 안바뀜 그대로 문자형은 변경 불가능 자료
#새로운 문자열 생성하여 넘겨줘야
s.count('t') # 1, t 몇번 사용됬는
s.startswith('py') # True
d = 'I love python'
s.split() # ['I', 'love', 'python']
words = s.split()
' '.join(words) # 'I love python'
':'.join(words) # 'I:love:python'
(1>2) and (2<3) # False
None # None 자료형은 객체 상수값, 숫자의 0같은 의미, 객체가 없다는 의미
int # <class 'int'>
float # <class 'float'>
str # <class 'str'>
int('123') # 123, 형변
int(1.23) # 1
float('2.3') # 2.3
float(3) # 3.0
str(3) # '3'
ord('1') # 49
