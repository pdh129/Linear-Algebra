# pytube 구글에쳐서 그냥 예제하나씩치면서 확인해보면됨
'''
from pytube import YouTube

print(YouTube('https://www.youtube.com/watch?v=2_uODrqH2aE'))
utube = YouTube('https://www.youtube.com/watch?v=2_uODrqH2aE')

# 스트림(stream)은 동영상을 다운받지않고 그냥 바로 다운받으면서 실행하는 것

print(utube.description) # 유튜브 영상 소개
print(utube.title) # 유튜브 영상 제목

k = utube.streams[0]
print(k)
# <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="6fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">
# 여러가지 유튜브 영상 정보가 나옴, vcodec = 비디오 코덱, acodec = 오디오 코덱 -> 비디오 오디오 따로실행해서 동기화시킴.


b = utube.streams
print(b) # stream의 전체 정보

for i, stream in enumerate(utube.streams): # enumerate는 for문하면서 index도 같이 넘겨줌
    if stream.type == 'video':
        print(i, stream.mime_type, stream.resolution, stream.fps) # video일 경우만 다음 정보가 있음
    if stream.type == 'audio':
        print(i, stream.mime_type, stream.abr) # audio일 경우만 다음 정보가 있음

c = utube.streams[3] # 3 video/mp4 1080p 25 이정보로 비디오만 다운로드
c.download()

d = utube.streams[16] # 16 audio/mp4 128kbps 이정보로 오디오만 다운로드
d.download()

# 파일이름, 경로도 지정해서 저장할 수 있음

bb = utube.streams.filter(mime_type='audio/mp4') # 오디오에서 mp4로 관련된 stream 정보만 필터거쳐 출력
print(bb)
'''

# 웹 브라우저 자동화, selenium 배우기, 브라우저 자동화를 위한 도구, pip install selenium

from selenium import webdriver # 파이썬이 직접 웹 브라우저를 컨트롤 하는 것이 아닌 사이의 중간다리 프로그램(웹드라이버)을 통해 컨트롤
# 그래서 그 중간다리 프로그램도 다운해야함, 구글크롬 드라이버 다운 해보자 https://chromedriver.chromium.org/getting-started
# 여기서 드라이버 설치할때 크롬 버전에 맞게 설치해야함, 112.0, 이때 설치는 파이썬 작업하는 디렉토리 폴더에 압축풀기

from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # 빈 크롬창이 뜸

driver.get('https://klas.kw.ac.kr/') # 크롬을 통해 klas에 들어감

# 이제부터 이 사이트를 자동화하자. 먼저 아이디 치는거 자동화하자

# F12로 개발자 툴 열고, 마우스클릭버튼으로 아이디 입력부분 클릭,

# <input type="text" id="loginId" value="" class="form-control ime-false" placeholder="ID" maxlength="20" title="로그인 아이디">

# 여기서 따서 써야함, id를 따보자

ele = driver.find_element(By.CSS_SELECTOR, '#loginId') # copy_selector
ele.click()
driver.find_element(By.CSS_SELECTOR, 

# 이번엔 비밀번호 부분

# <input type="password" id="loginPwd" class="form-control ime-false" placeholder="PASSWORD" maxlength="10" size="10" title="로그인 비밀번호">

ele = driver.find_element(By.CSS_SELECTOR, '#loginPwd')
ele.click()

# ele.click()은 element 찾아서 클릭
