from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'''
myid = 'xxxx'
mypwd = 'xxxx'


driver = webdriver.Chrome()
driver.get('https://klas.kw.ac.kr')
ele = driver.find_element(by='id', value='loginId')
ele.send_keys(myid)

ele = driver.find_element(by='id', value='loginPwd')
ele.send_keys(mypwd+'\n')

# 맨위과목 공지사항 F12로 클릭 -> 우클릭 -> copy -> copy selector

ele = driver.find_element(By.CSS_SELECTOR, '#appModule > div > div:nth-child(1) > div:nth-child(2) > ul > li:nth-child(1) > div.right > button.btn2.btn-lightgreen.btnsmall')
ele.click()

# 공지사항 들어가기

driver.back()

# 크롬에서 뒤로가기

ele = driver.find_elements(By.CSS_SELECTOR, '#appModule > div > div:nth-child(1) > div:nth-child(2) > ul > li > div.right > button.btn2.btn-lightgreen.btnsmall')

# 모든과목 공지사항 ele에 저장

print(len(elems))

# 과목수 확인

elems[1].click()

# 파이썬프로그래밍기초 공지사항들어가기

trs = driver.find_elements(By.CSS_SELECTOR, '#appModule > table > tbody > tr')
for tr in trs:
    tr
    row = [td.text for td in tr.find_elements(By.TAG_NAME, 'td')]
    rows.append(row)

print(rows)

# 각 공지사항 안에 텍스트 row에 넣고 모든 공지사항의 row를 합쳐 row에 넣어 출력

ele = driver.find_element(By.CSS_SELECTOR, '#navbarHeader > div > div > div:nth-child(2) > ul > li:nth-child(1) > ul > li:nth-child(4)')
ele.click()

# 강의자료실 들어가기


elems = driver.find_element(By.CSS_SELECTOR, '.lft')

# .은 class를 의미 .lft인 class를 다찾음 -> CSS_SELECTOR의 문법임
# 강의자료실에 있는 모든 강의자료 다운하기 위해 찾음

elems[0].click

# 첫번째 강의자료 클릭

import time

ele = driver.find_elements(By.CSS_SELECTOR, '.board_viewfile')
for a in ele.find_element(By.TAG_NAME, 'a'):
    a.click()
    time.sleep(1)

# 1초간격으로 class가 board_viewfile인거 다찾아서 태그가 a인거 클릭
# 여기선 강의자료안에 모든 자료 다클릭해서 다운
# 만일 다운할 자료가 없을 수 있으니 에러 확인해서 예외처리도 해야함

ele = driver.find_elements(By.CSS_SELECTOR, '#navbarHeader > div > div > div:nth-child(1) > ul > li:nth-child(1) > ul > li:nth-child(1)')
ele.click()

# 수업시간표 클릭

ele = driver.find_elements(By.CSS_SELECTOR, '.scheduletb')

# class가 scheduletb인 수업시간표 테이블 찾기

ele.get_attribute('innerHTML')
# 위의 테이블 안에 있는 HTML 정보 찾기

drier.close()

# 구글 크롬창 닫기

# 여기까지 klas사이트 관련해서 실습 이제부터 네이버 실습


myid = 'xxxx'
mypwd = 'xxxx'

driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

ele = driver.find_element(by='id', value='id')
ele.send_keys(myid)

ele = driver.find_element(by='id', value='pw')
ele.send_keys(mypwd+'\n')
'''

# 네이버는 이렇게 로그인하면 자동입력 방지 뜸. 매크로로 인식함.

import pyperclip

myid = 'pdh6608'
mypwd = 'younghui12'

driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

ele = driver.find_element('id', 'id')
ele.click()
pyperclip.copy(myid) # id를 클립보드에 copy
ele.send_keys(Keys.CONTROL, 'v') # ctrl+v를 key로 보냄 id를 붙여넣기하는것

ele = driver.find_element('id', 'pw')
ele.click()
pyperclip.copy(mypwd) # id를 클립보드에 copy
ele.send_keys(Keys.CONTROL, 'v') # ctrl+v를 key로 보냄 id를 붙여넣기하는것

ele = driver.find_element(By.CSS_SELECTOR, '#log\.login > span')
ele.click()

