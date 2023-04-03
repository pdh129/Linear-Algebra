import requests
url = 'http://naver.com'
r = requests.get(url)
print(type(r)) # requests.models.Response 자료형 -> 자료형은 결국 class 그자체
#r은 class의 객체 object
print(r) # <Response [200]> : 클라이언트가 서버에 Request(요청)하면 서버가 Response(응답)하여 데이터를 줌
# 200은 정상적으로 서버가 응답해서 데이터를 줬다는것.
# 404는 에러를 뜻함. 요청한 자료를 찾을 수 없을 때
# 503(?)은 외국에서 접속할 수 없을 때
print(r.status_code) # 위의 상태 숫자만 출력
print(r.text) # html 문서를 출력함, 서버에서 준 데이터
#html 문서를 받아 웹브라우저가 받아서 이미지로 출력함
print(r.encoding) # UTF-8로 인코딩 됨을 확인가능, 디코딩을 UTF-8로 확인해야 한글 볼 수있음
# 인코딩 디코딩 코덱이 같아야 글자가 안깨짐
'''
r.encoding = 'utf-8'  로 수정
'''

open('test.txt', 'w').write('testing') # 파일 만들고 testing 씀
#open은 파일 객체를 넘겨줌
#어디에 저장되는지 확인법
import os
print(os.getcwd()) # 현재 작업 디렉토리 확인

'''
open('naver.html', 'w').write(r.text) # UnicodeEncodeError 오류뜸
# 한글이 발생하는 문제, 'cp949' codec can't encode character '\U0001f923' in position 83869: illegal multibyte sequence
#cp949 코덱을 utf-8로 바꿔야함. 인코딩 지정해줘야함
'''
open('naver.html', 'w', encoding='utf-8').write(r.text) # utf-8 코덱 지정


# 이미지 저장하기
url2 = 'https://voicebot.ai/wp-content/uploads/2021/07/cp-head-square.png'
r2 = requests.get(url2)
print(r2) # 이미지는 bytes형
# 이미지는 r.text가아닌 r.content로 불러오기
# r.text는 이미지를 텍스트로 해석, 이미지를 그자체로 해석하려면 content
# 'rb' 'rt' 차이임
# byte 자료형으로 불러옴
print(type(b'abc')) # bytes형 자료
print(b'abc') # 현재는 byte형 자료형
print(b'abc'.decode()) # 디코딩을 통해 byte 형을 문자로봄
print('abc'.encode()) # 인코딩을 통해 문자를 byte 형으로봄

print('abc한글'.encode('utf-8')) # 디코딩도 똑같이 utf-8로해야 abc한글이보임
print('abc한글'.encode('cp949')) # 마찬가지로 디코딩 cp949

print(r2.content) # byte형태로 보여줌
open('copilot.png', 'wb').write(r2.content) # w는 문자용, wb로 이미지저장

#대용량에 경우 request가 데이터 받을때 일정량(chunk, 청크)씩 받아서
#부분적으로 저장. ex)4GB자료면 4KB씩 받아서 부분적으로 계속 저장

#1960~1961년 날씨 1~12월 저장
import time
url3_template = 'https://www.weather.go.kr/w/obs-climate/land/past-obs/obs-by-day.do?stn=108&yy={}&mm={}&obs=1'
for yy in range(1960,1961):
    for mm in range(1, 13):
        url3 = url3_template.format(1980, mm) # {}, {}에 넣는 것 브레이스 처리한거에넣음
        r3 = requests.get(url3)
        fpath = 'C:/Users/kw/Desktop/{}_{}.html'.format(yy, mm)
        open(fpath, 'w', encoding='utf-8').write(r3.text)
        print(fpath)
        time.sleep(0.5) # 서버에 갑자기 엄청요청하면 디도스로받아들임 시간차 요청
