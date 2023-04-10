from bs4 import BeautifulSoup

html = open('w 1960_4.html', encoding = 'utf-8').read()
soup = BeautifulSoup(html)
'''
print(soup)
print(type(soup)) # bs4.BeautifulSoup라는 패키지가 나옴(아래 하위 모듈많음)
# 1개의 파일을 모듈, 2개 이상을 패키지라함 사용법은 둘다 같음
# bs4에 저장되어있는 모듈
print(soup.title) # html 문서에서 title만 따옴
print(soup.head) # head 따옴
print(soup.title.find_next()) # soup.title이 또 객체가되어 함수사용가능
print(soup.find('title')) # find로 title 태그 찾기
print(soup.find('p')) # p 태그 중 맨 위에있는거 찾기
print(soup.find_all('p')) # p 태그 싹다 찾기
print(soup.find_all('strong')) # strong(글씨 강조체) 태그 다 찾기
print(soup.find_all('strong', 'spot')) # 많은 strong 태그 중 spot이라는 class 있는애 찾음(필터링)
print(soup.find_all('strong', attrs={'class' : 'spot'})) # attrs를 통해 속성값 지정해줄 수 있음
print(soup.select('strong')) # strong 태그 다찾아줌
print(soup.select('.spot')) # class가 spot인것만 찾음, css언어 스타일임
print(soup.select('#lnb')) # id = lnb인 태그 찾기, 마찬가지로 css언어
# .~ class찾기, #~ id 찾기
'''
print(soup.select('body > div.container > section > div > div.cont-wrap > div.cmp-past-obs > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td:nth-child(6) > span:nth-child(4)'))
# 최고기온에 관한 span태그 다 따옴, select는 css언어에서 사용하는 문법을 이용함,
# 경로얻는법 크롬들어가서 F12, 마우스커서같은거클릭, 원하는 부분 클릭, 마우스우클릭, copy
print(soup.select('body > div.container > section > div > div.cont-wrap > div.cmp-past-obs > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td:nth-child(6) > span'))
# 하루치정보 다나옴

spans = soup.select('body > div.container > section > div > div.cont-wrap > div.cmp-past-obs > div:nth-child(3) > div > table > tbody > tr:nth-child(2) > td:nth-child(6) > span')
text_list = [span.text for span in spans if span.text] # text형태로 띄어쓰기 없이 저장
text_list_split = [e.split(':') for e in text_list] # list 형태로 저장
text_list_split_dic = dict([e.split(':') for e in text_list]) #  dict 형태로 변환
print(text_list)

tr_list = soup.select('body > div.container > section > div > div.cont-wrap > div.cmp-past-obs > div:nth-child(3) > div > table > tbody > tr')
tr0 = tr_list[0]
print(tr0.select('td')) # 몇일인지 나옴
tr1 = tr_list[1]
print(tr1.select('td')) # 온도 나옴
dates_tr = tr_list[::2]
temps_tr = tr_list[1::2]
print(dates_tr) # index중 0, 2, 4, 6 이런거를 통해 날짜만 뽑아냄 (짝수 index 뽑기)
print(temps_tr) # index중 1, 3, 5, 7 이런거를 통해 날씨,온도만 뽑아 (홀수 index 뽑기)

tr2 = dates_tr[0]
real_dates = [e.text.strip() for e in tr2.select('td')] # 첫번째 행에서 진짜 날짜만 딱뽑아서 리스트로 만듬
print(real_dates) # 결과로 ['', '', '', '', '', '1일', '2일']
tr3 = temps_tr[0]
real_temps = [e.text.strip() for e in tr3.select('td')] # 첫번째 행애서 날씨,온도만 딱뽑아서 리스트로 만
print(real_temps)

# 이제 첫번째 행에서 각 일마다 대해 날짜와 온도 매칭
real_data = dict(list(zip(real_dates, real_temps)))
print(real_data)

# 이제 위에걸 행만큼 반복하면 전체 날짜와 온도 뽑아낼 수 있음
temp_table = {}
for tr_date, tr_temp in zip(dates_tr, temps_tr):
    dates = [e.text.strip() for e in tr_date.select('td')]
    temps = [e.text.strip() for e in tr_temp.select('td')]
    temp_table.update(dict(list(zip(dates, temps))))
print(temp_table)
