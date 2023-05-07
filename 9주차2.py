# 파일 및 자료형의 입출력

# 텍스트 파일 입출력

f = open('test.txt', 'w')
f.write('파일 입출력 시험 중입니다.\n')
f.write('몇 번이고 호출 가능합니다.\n')
f.close()

import glob

glob.glob('*.txt') # 파일 잘 생성되있는지 확인 or os.exist 사용

f = open('test.txt', 'r') # default read여서 'r'생략가능 open('test.txt')
txt = f.read() # 파일 안의 내용 전부 가져오기
f.close()
print(txt)

# txt = open('test.txt').read() 이렇게하면 파일객체 따로 저장안해서 close안해도됨


# with문 이용하기 with <expression> as <variable>: <block>

with open('test.txt', 'w') as f: # 파일객체를 f로 사용하겠다는의미
    f.write('파일 입출력 시험 중입니다.\n')
    f.write('몇 번이고 호출 가능합니다.\n')

# with문을 이용하는 장점은, 파일 입출력 작업이 블록화되어 코드를 읽기 좋다는
# 점과, with문을 빠져나오면서 파일 객체를 자동으로 close()해준다는 것.
# 파일 입출력은 가능하면 with문을 이용하는 것이 좋다.

with open('test.txt') as f:
    txt = f.read()


# 파일 안의 내용 라인 단위로 읽기

with open('test.txt') as f:
    for line in f: # 파일객체 for문에 넘겨주면 자동으로 라인 단위로 읽힘
        print(line.rstrip()) # rstrip()은 각 줄의 \n 삭제


# 파일에 내용 추가하기

with open('test.txt', 'a') as f:
    f.write('한 줄 더 추가해 봅니다')

# test.txt가 없으면 새로 만들고, 있다면 기존 파일 제일 끝에 내용 추가

print(open('test.txt').read())


# encoding 옵션

# 파일을 열 때 UnicodeDecodeError 에러가 발생할 때 가있음

# 윈도우는 기본 cp949, 최근 많은 파일들은 utf-8 형

txt = open('data/대한민국헌법.txt').read() # 오류남

txt = open('data/대한민국헌법.txt', encoding='utf-8').read()

# 한글은 대부분 c949 아니면 utf-8로 인코딩 되어 있


# 이미지 파일 읽고 쓰기

# byte 자료형이며 b''와 같이 표현됨
print(b'binary data') # bytes

# 문자열 자료형도 바이트 자료형으로 변환 가능

s = '좋은 하루입니다'
s.encode('utf-8') # default 값이 utf-8

s.encode('euc-kr')

# 1바이트의 16진수 코드로 encode

b = s.encode() # default는 utf-8
b.decode('utf-8')


# 이제 이미지 파일 처리
# 파이썬 메인 이미지로 학습

with open('img\\python.png', 'rb') as f:
    im = f.read()

print(im[:20]) # 첫 줄만 확인

# 이미지 처리 모듈
# Pillow, opencv-python

from PIL import Image

image = Image.open('img/python.png')
image.show()

image.size # 이미지 사이즈 확인

small_img = image.resize((300, 100)) # 이미지 작게 만들기 가능, 튜플로 넘겨줌
small_img.show()

small_img.save('python_small.png') # 이미지 저장


# 오디오 파일 읽고 쓰기

# 오디오 파일도 이진파일임. 'mp3'파일의 파형을 그려보는데
# 'mp3'는 압축파일이여서 raw파일 같은 'wav'로 변환해야 그려볼 수 있

# pydub 모듈 사용

from pydub import AudioSegment

sound = AudioSegment.from_mp3("data/standbyme.mp3") # 파일 읽기
sound.export("standbyme.wav", format="wav") # wav로 바꿔 파일 저장

# wav파일 읽기 위해 scipy 모듈 사용
# numpy를 이용해서 상위 레벨의 수학연산을 지원하는 모듈

from scipy.io import wavfile

samplerate, data = wavfile.read('standbyme.wav')
print(samplerate) # 44100

# 샘플링 주파수가 44100Hz라는 소리

# 파형은 data에 저장되어있는 자료형이 numpy의 array형

type(data) # numpy.ndarray

data.shape # (7832576, 2)
# 2차원 배열임, 샘플 수가 7832576개이고 2채널(왼쪽, 오른쪽 채널)스테레오라는 의미

print(7832576 / 44100) # 177.6094 나오는데 거의 3분짜리의 음악이라는 뜻

ch1 = data[:, 0] # left 채널 데이터 값만 저장

ch1[100000:100010] # 일부(0.5초)만 그려봄

import matplotlib.pyplot as plt

plt.plot(ch1[20000:20000+44100//2]);
plt.grid()
plt.show()

sampling_rate = 44100
wavfile.write('test.wav', sampling_rate, data) # 오디오 파일 저장

# 파이썬 객체 저장하기(pickle)

# 사전, 리스트, 튜플, 집합 등의 자료를 파일에 저장해야할 때도 있음

# pickle은 파이썬 기본 모듈

book1 = {'제목' : '한번 배운 파이썬, 나만의 활용 스킬'}
book2 = {'제목' : '미적분으로 바라본 하루'}
books = [book1, book2]

import pickle

pickle.dump(books, open('books.pickle', 'wb')) # books라는 파일 객체를 그대로 저장

pickle.load(open('books.pickle', 'rb')) # 그 저장한 파일을 그대로 읽음

# 반드시 binary모드로 저장, 읽기

# 파이썬 객체 저장하기(json)
# 또다른 방법

# json은 자바스크립트에서 정의된 데이터 교환을 위한 텍스트 파일 포맷.

import json
json.dump(books, open('books.json', 'w'))
json.load(open('books.json'))

# pickle과의 차이점은 binary모드가 아닌점

data = {1: ('one', '하나'), 2: ('two', '둘'), 3: ('three', '셋')}

json.dump(data, open('test.json', 'w'))
json.load(open('test.json'))

# 문제는 자바스크립트에는 key로 숫자를 사용할 수 없고
# 튜플이 없음 그래서 위처럼 파이썬에서 튜플과 숫자 키를 저장하면\
# load시 숫자는 텍스트로 바뀌고 튜플은 리스트로 바뀜
# 가장 유사한 형태로 바뀌어 자바스크립트로 저장됨

# 그래서 순수하게 파이썬 객체 저장하려면 pickle을 사용하고
# 다른 프로그램이 언어와 호환하기 위해 저장하려면 json포맷을 사용
# 대부분 언어가 json을 쓰기때문


# 파이썬 객체 저장하기(shelve)
# shelve 모듈은 데이터가 많아서 메모리에 다 올려놓고 사용하기 부담스러울 경우

import shelve

# 예를들어, 앞서 사용된 사전 자료에서 'ISBN13'코드에 해당하는 이미지 정보를 저장하고 싶

isbn13 = '9788965402770'
with oepn('img\\python.png', 'rb') as f:
    im = f.read()

# 등록된 책 정보가 너무 많다면 이 데이터를 사전으로 파있너 객체로 저장해서 메모리에 두기는 부담스러움

book_image = {}
book_image[isbn13] = im # 이런식으로하면 메모리에 저장됨

# 그렇다고 이미지들을 별도의 파일로 관리하는 것도 안 좋아보임

with shelve.open('bookimage.shelve') as bk:
    bk[isbn13] = im

# 이렇게하면 메모리가아닌 파일에 key와 value가 저장되어있음

with shelve.open('bookimage.shelve') as bk:
    im2 = bk['9788965402770']

print(im2)
# 바이너리 형태 이미지 출력됨

from IPython.display import Image
import io

im2_bytesio = io.BytesIO(im2)
Image(im2_bytesio.getvalue()) # 이미지로 출력

# 결국 장점은 사전 형식을 사용하지만, 파일 시스템으로 관리되고 있으므로
# 메모리 부담 없이 필요한 정보만 뽑아낼 수 있다.

