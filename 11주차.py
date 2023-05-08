import imapclient
from datetime import date, timedelta

uid = ''
pw = ''

imap = imapclient.IMAPClient('imap.naver.com', ssl=True)
imap.login(uid, pw) # 로그인
imap.list_folders() # 메일함
imap.select_folder('INBOX', readonly=False) # 폴더 선택
mids1 = imap.search(['ALL']) # 메일 번호형태로 전부 나옴
mids2 = imap.search(['UNSEEN']) # 않읽은 메일
mids3 = imap.search(['ON', data.today()]) # 오늘 온 메일
mids4 = imap.search(['ON', date(2023, 5, 7)]) # 특정 날짜에 온 메일
mids5 = imap.search(['SINCE', date.today() - timedelta(days=7)]) # 오늘부터 7일전까지 메일
mids6 = imap.search(['BEFORE', date.today() - timedelta(days=7)]) # 7일전 이전에 온 메일
mids7 = imap.search(['FROM', '메일']) # 특정메일로 부터 온 메일
mids8 = imap.search(['SUBJECT', '제목']) # 특정제목 메일
# 문제는 제목이 한글이 안됨, 영어만 잘됨
# imapclient폴더에 util.py 32번째 줄 수정해야함

# def to_bytes(s, charset="ascii"):
#   if isinstance(s, text_type):
#       return s.encode(charset)
#   return s

# 아스키 코드는 한글 오류가 있음

%debug # 직접 디버그해서 버그난데 직접들어가서 확인
# ipdb> charset
# 'us-ascii'
# ipdb> q # 빠져나오기

# def to_bytes(s, charset="utf-8"):
#   if isinstance(s, text_type):
#       return s.encode("utf-8")
#   return s

# 이번에는 imapclient.py 1705번째 오류

# if b"LITERAL+" in self._chaced_capabilities:

# self._chaced_capabilities 이 값이 NONE이 나오는 오류

%debug
# ipdb> print(self._chaced_capabilities)

# self._chaced_capabilities: and if b"LITERAL+" in self._chaced_capabilities:

# NONE이 아닐 경우만 실행

# 이제 한글 도됨

mids9 = imap.search(['SUBJECT', '(광고)', 'BEFORE', date.today() - timedelta(days=7)]) # 제목 (광고)들어가면서 7일전 이전에 온 메일
imap.delete_messages(mids9) # 삭제
imap.expunge() # 휴지통에서도 없애는 효과느낌 (gmail은 필수)

mids10 = imap.search(['ON', data.today()])
rmsgs = imap.fetch(mids10[0], ['BODY[]']) # 오늘온 메일 중 첫번째 메일 내용 가져옴
# 이때 위의 내용은 통신을 위한 base64 형태
# base64란 알파벳 소문자+대문자 = 52개 + 숫자 10개 + 어떤 문자 2개
# 이렇게 64개를 문자세트로 만듬
# 내가 보내는 문자는 8bit 씩 보냄 base64는 6bit씩
# 그러면 24bit당 4개의 문자로 인코딩 된 형태임
# 어쨋든 통신을 위한 문자형태로 바꿔버림

rmsgs[mids10[0]][b'BODY[]'] # 본문 내용

import pyzmail36 # pip install pyzmail36 or pip install pyzmail
# 위 이메일을 해석하는 도구

import pyzmail

msg = pyzmail.PyzMessae.factory(rmsgs[mids10[0]][b'BODY[]'])# 해석한 메일 통째로 넣음
msg.get_address('from') # 누구한테 온지 알 수 있음
msg.get_address('to') # 누구에게 보낸지 알 수 있음
msg.get('Date') # 메일 온 날짜
msg.text_part.get_payload() # 본문을 그대로 가져옴(아직 bite 형태), 인코딩된상태
msg.text_part.get_payload().decode(msg.text_part.charset) # 본문 디코딩까지
msg.text_part.charset # 이거는 메일의 인코딩된 형태 ex) "utf-8"
