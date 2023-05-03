L = ['123', '54', '36', '2', '9', '8', '4']
L.sort()
print(L)
# ['123', '2', '36', '4', '54', '8', '9']
# 문자열 정렬은 문자열의 맨 처음 문자를 기준으로 정렬

# 위에 문자를 숫자로 보려면 어떻게 정렬해야 하는가?

# key 인수를 이용한 정렬
# key는 함수를 지정하는 인수

def mykey(ele):
    return int(ele)

L.sort(key=mykey) # 비교를 할 때 key에서 지정한 함수를 거친 요소로 정렬
print(L)
# ['2', '4', '8', '9', '36', '54', '123']


L.sort(key=int) # 그냥 이렇게 int()함수 바로전달해도됨

L.sort(key=int, reverse=True) # 내림차순

# 람다(lambda) 함수
# def~ 이런 함수는 문이라고함. 자체적으로 어떤 값을 넘기는게 아님
# 람다는 표현식임, 어떤 계산식의 결과값을 넘기는 표현식임

f = lambda e: int(e)
print(f('123'))
# 123
# e: int(e)는 e라는 객체를 받아서 int(e)함수를 거친 값을 return

add = lambda a, b: a+b # 객체 2개받는것도 가능
print(add(2, 3))


L.sort(key=lambda e: int(e)) # 각요소가 람다 함수를 거친후의 값을 기준으로 정렬

L = ['7:27', '14:22', '6:9', '6:11', '2:19'] # 시간:분
L.sort()

def f(e):
    return int(e.split(':')[0]), int(e.split(':')[1])
# '7:27'을 ':'을 기준으로 나눠서 0번째 요소와 1번째 요소 return

L.sort(key=f) # 이렇게하면 시간 별로 오름차순 정렬

L.sort(key=lambda e: (int(e.split(':')[0]), int(e.split(':')[1])))


# 파일 이름 정렬
flist = ['py_123.txt', 'py_54.txt', 'py_36.txt', 'py_2.txt', 'py_9.txt']
flist.sort()

# 파일이름을 숫자를 기준으로 정렬해보자

import os
fname = 'py_123.txt'
os.path.splitext(fname) # 파일 확장자랑 이름 분리하는 함수
# ('py_123', '.txt')
os.path.splitext(fname)[0].split('_')
# ('py', '123')
int(os.path.splitext(fname)[0].split('_')[1])
# 123

def mykey(fname):
    return int(os.path.splitext(fname)[0].split('_')[1])
flist.sort(key=mykey)
flist

# 이번에는 파일이름에 경로명 까지 포함될 경우
import glob
flist = glob.glob('data/py*.txt') # data 폴더안에 py로 시작하는 .txt파일들
print(flist)
'''['data\\py_002.txt',
    'data\\py_009.txt',
    'data\\py_036.txt',
    'data\\py_054.txt',
    'data\\py_123.txt']
 '''
flist.sort(key=mykey)
print(flist)

'''['data\\py_002.txt',
    'data\\py_009.txt',
    'data\\py_036.txt',
    'data\\py_054.txt',
    'data\\py_123.txt']
 '''

# 근데 mykey함수도 불안함 왜냐하면 상위 폴더에 _가 있을 수도 있어서

fpath = 'data\\py_123.txt'
os.path.split(fpath)
# ('data', 'py_123.txt') 경로명과 파일명 따로 나눠짐

def mykey(fpath):
    fname = os.path.split(fpath)[1]
    return int(os.path.splitext(fanme)[0].split('_')[1])
flist.sort(key=mykey)

# sorted() 함술르 이용한 정렬
# sort는 메서드라고 객체에 딸린 함수, sorted()는 그냥 함수임. return값도 있음.
# sorted는 원래 객체는 안건들임, 새로운 정렬한값 return
L = ['123', '54', '36', '2', '9', '8', '4']
a = sorted(L)
print(L)
# ['123', '54', '36', '2', '9', '8', '4']
print(a)
# ['123', '2', '36', '4', '54', '8', '9']
b = sorted(L, key=int)
print(b)
# ['2', '4', '8', '9', '36', '54', '123']
c = sorted(L, key=int, reverse=True)


# 파이썬으로 파일과 폴더 다루기

# 파일 목록 얻기
# 여러 방법이 있지만 그중 glob방법 사용
# glob 모듈의 glob(pathname)함수를 사용하는 것
# 인수 pathname에 와일드카드 문자를 사용할 수 있음
# 와일드카드 문자는 여러 파일을 한번에 찾으려 할 때 사용할 수 있는 메타 문자를 의미
# glob()함수에 사용가능한 와일드카드 문자는 다음과 같음
# ? : 임의의 문자 1개와 일치합니다.
# * : 임의의 개수(0개 포함)의 모든 문자와 일치합니다.
# [...] : 괄호 안의 임의의 1개 문자와 일치합니다.

import glob
glob.glob("C:\\Windows\\*.exe") # .exe 파일 모두 골라내기
glob.glob("C:\\Windows\\[bc]*.*") # b 혹은 c로 시작하는 모든 파일 골라내기
# *.* 확장자나 이름이 아무거나인 모든파일 앞에 [bc]를 붙여준것.
glob.glob("C:\\Windows\\??.exe") # 두글자.exe인 파일 골라내기

import os
os.listdir('C:\\Windows') # Windows 폴더안 모든 파일을 리스트로 return

# glob는 return할 때 파일경로+파일명.확장자을 return하지만
# os는 return할 때 파일명.확장자만 return

# 파일 이름 변경
glob.glob('data/p*.txt')
'''
['data\\py_123.txt',
 'data\\py_2.txt',
 'data\\py_36.txt',
 'data\\py_54.txt',
 'data\\py_9.txt']
'''
# 목적은 py_2면 py_002처럼 3글자로 변경

import os

fpath = 'data\\py_2.txt'
path, fname = os.path.split(fpath) # 경로와 파일명 분리
print(path)
# 'data'
print(fname)
# 'py_2.txt'

head, tail = os.path.splitext(fname) # 파일명에서 확장자랑 이름 분리
print(head)
# py_2

heads = head.split('_') # 이름에서 _를 기준으로 또 분리
print(heads[1])
# '2'

n = int(heads[1])
print('{:03}'.format(n)) # 정수로 변환하고 세자리 문자열로 맞춤
# '002'

fname2 = '{}_{}{}'.format(heads[0], '{:03}'.format(n), tail)
print(fname2)
# 'py_002.txt'

fpath2 = os.path.join(path, fname2) # join으로 경로 두개 합침
print(fpath2)
# 'data\\py_002.txt'

os.rename(fpath, fpath2) # 파일 이름 변경하는 메소드

# 자 이제 코드 다합치면
import os
import glob
for fpath in glob.glob('data/*/txt'):
    path, fname = os.path.split(fpath) # 경로와 파일명 분리
    head, tail = os.path.splitext(fname) # 파일명에서 확장자랑 이름 분리
    heads = head.split('_') # 이름에서 _를 기준으로 또 분리
    n = int(heads[1])
    fname2 = '{}_{}{}'.format(heads[0], '{:03}'.format(n), tail)
    fpath2 = os.path.join(path, fname2) # join으로 경로 두개 합침
    print(fpath, '==>', fpath2)
    os.rename(fpath, fpath2) # 파일 이름 변경하는 메소드

print(glob.glob('data/*.txt')) # 바뀐 이름 확인, 윈도우 자체적으로 오름차순 정렬도됨

# 파일 복사
# 여러 파일 복사는 for문을 이용하여 하나씩 해야함.

import shutil

shutil.copyfile('data/py_002.txt', 'data/data_002.txt')
# 왼쪽 소스 파일을 오른쪽 경로에 파일명으로 복사

shutil.copy('data/py_002.txt', 'e:/') # 소스 파일 이름 변경 없이 디렉토리만 지정하여 복사

shutil.copytree('data', 'backup') # data라는 디렉토리를 통째로 backup으로 복사
# 하위 디렉토리도 싹다 복사

# 이번엔 backup2 디렉토리에 일부파일만 복사
import os
import glob
import shutil

if not os.path.exists('backup2'): # 일단 backup2 폴더 존재 확인
    os.makedirs('backup2') # 폴더 만들기, C://Windows~/backup2와 같이 앞에 경로 안해줘도됨

for fpath in glob.glob('data/py*.txt'):
    shutil.copy(fpath, 'backup2')

# 파일 이동
shutil.move('data/py_002.txt', 'backup') # 파일 이동

# 파일 하나 삭제
os.remove('backup2/py_002.txt')

# 디렉토리(폴더) 통째로 삭제
shutil.rmtree('backup2') # 하위 디렉토리까지 모두 삭제

# os.walk(top_dir)는 하위 디렉토리를 재귀적으로 모두 탐색하면서 파일 목록을 얻게 해줌
# 인수 top_dir에서 시작하여 하위 디렉토리를 검색해 가면서 디렉토리 목록과
# 파일 목록을 반복적으로 전달하며, 반환 형식은 튜플 (dirpath, dirnames, filenames)

import os

for curdir, dirs, files in os.walk('.'): # 현재 디렉토리('.')를 중심으로 하위 디렉토리 탐색
    print('curdir=', curdir) # 현재 디렉토리
    print('dirs=', dirs) # 하위 디렉토리 목록
    print('files=', files) # 하위 파일 목록
    print('-'*60)

# 문제 : 하위 디렉토리의 모든 파일을 검색해서 현재 시간을 중심으로 24시간 이내에
# 수정된 파일 목록을 출력하라.
# os.path.getmtime(fpath)를 이용하면 파일의 수정 시간(초)를 얻을 수 있음
# time.time()을 이용하면 현재 시간(초)를 얻을 수 있음

import time
import os

curtime = time.time()
file_modified_time = os.path.getmtime(fpath)
