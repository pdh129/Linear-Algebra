import pyautogui # 마우스, 키보드를 제어할 수 있게 해주는 모듈
import time
'''
#pyautogui모듈
print(pyautogui.size()) #이름이 있는 tuple을 return함
s = pyautogui.size()
print(type(s)) # type가 모듈에 있는 Size라는 type으로 뜸
w, h = pyautogui.size()
print(w) # 일반 튜플처럼 언패킹도 가능하고 indexing도 가능
print(h)
print(s[0])
print(s[1])
pyautogui.moveTo(100, 100, duration=1) # (100, 100)으로, duration = 1초동안 마우스를 이동해라
pyautogui.click() # 마우스클릭
print(pyautogui.position()) # 현재 마우스 좌표 이름이 있는 tuple로 return
# 계산기 켜서 맨왼쪽위에 갖다두고 각 버튼 마우스 좌표 찾기
'''
# time모듈
'''
time.sleep(2)
for i in range(5):
    print(pyautogui.position())
    time.sleep(2) # 2초 기다리고 그다음 반
    '''
'''
time.sleep(2)
x, y = pyautogui.position() # 맨왼쪽아래 +/-에 마우스 올려 시작점 좌표
dx = 90
dy = -50

for i in range(6): # 맨아랫줄 버튼4개좌표
    print(i+1,'줄')
    for j in range(4):
        print((i+1,j+1),x + dx*j, y + dy*i)
'''
btns = { '1' : (33, 454), '2' : (123, 454), '3' : (213, 454), '4' : (33, 404), '5' : (123, 404),
         '6' : (213, 404), '7' : (33, 354), '8' : (123, 354), '9' : (213, 354), '+' : (313, 454),
         '=' : (313, 504)}

exp = '12+2111='
for c in exp: # in에는 반복가능한 모든 데이터 올수있음, 문자열도 반복가능한 자료라 가능
    x, y = btns[c]
    pyautogui.click(x, y)
