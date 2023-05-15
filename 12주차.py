# 이미지 처리 할 때 Pillow 자주쓰임

import glob

flist = glob.glob('C:/Users/kw/Desktop/*.jpg')
fpath = flist[0]

from PIL import Image # 파이썬 기본 이미지

img = Image.open(fpath) # 경로에있는 이미지를 파이썬 이미지 형태로 객체 생성
print(img.size) # 이미지 사이즈
print(img.mode) # 이미지 형태 확인(RGB)
print(img.format) # 이미지 확장자 확인
img.thumbnail((512, 512)) # 이미지를 사이즈 변경, 최대 범위 512, 512로 비율에 맞게 축소
print(img.size)

# jpg 파일에는 이미지정보 뿐만아니라 EXIF(메타정보)라는게 있음, 사진에 관련된 정보임
# 구글에 EXIF table 참조

from PIL import ExifTags
'''
print(ExifTags.TAGS) # 사전형태로 EXIF 태그 설명이 저장되어있음

print(img.getexif()) # 사진의 EXIF 정보 사전형태로 저장되어있음

# 태그마다 뭘 의미하는지 분석

for tag, value in img._getexif().items():
    print(tag, ExifTags.TAGS[tag], value) # 이미지에 EXIF 태그에 설명 붙여서 출력
'''

# 36867 : DateTimeOriginal로 분류

import os
import shutil

base_folder = 'C:/Users/kw/Desktop/Pictures'
for fpath in flist:
    fname = os.path.split(fpath)[1]
    img = Image.open(fpath)
    datetime_org = img._getexif()[36867]
    year = datetime_org.split()[0].split(':')[0]
    date = datetime_org.split()[0].replace(':', '-') # : 을 - 로 바꿈
    print(date)
    folder = os.path.join(base_folder, year, date) # 저장할 폴더경로
    if not os.path.exists(folder):
        os.makedirs(folder) # 폴더가 존재하지 않으면 폴더생성
    print(folder)
    dest = os.path.join(folder, fname) # 전체 경로
    print(dest)
    shutil.copyfile(fpath, dest) # 파일 복사

fpath = 'C:/Users/kw/Desktop/Pictures/2018/2018-02-02/20180202_120156.jpg'
img = Image.open(fpath)
print(img._getexif()[0x8825]) # GPS 태그 정보 확인
print(img._getexif()[0x8825][2]) # 북위 어딘지 확인
def dms2deg(data): # d, m, s를 각도로 변환
    d, m, s = data
    return float(d + m / 60 + s / 3600)
lat = dms2deg(img._getexif()[0x8825][2]) # 위도 좌표
lon = dms2deg(img._getexif()[0x8825][4]) # 경도 좌표

url = 'https://www.google.co.kr/maps/place/{},{}'.format(lat, lon) # 구글맵으로 실제 위치 확인
print(url)

os.startfile(url)
