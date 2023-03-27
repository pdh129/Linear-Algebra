if True:
    print('true')
if False:
    print('true')
if 1 > 3:
    print('true')
if 1 < 3:
    print('true')

s=60
if s >= 70:
    print('pass')
elif s >= 50:
    print('try harder')
else:
    print('fail')

a, b = 10, 20
result = 1 if a > b else 0 # 한줄짜리 if문
print(result)

print('\n\n')

for name in ['고양이', '강아지', '송아지']:
    if name.startswith('강'): # '강'으로 시작하면 참
        break # for문을 빠져나오는 것
    print(name)
else: # for의 else는 위 for문을 정상적으로 실행완료했으면 else를 실행하라는 뜻
    print('done')

print('\n\n')

for name in ['고양이', '강아지', '송아지']:
    if name.startswith('강'): # '강'으로 시작하면 참
        continue # for 아래 실행하지않고 다음 반복 시작
    print(name)
else: # for의 else는 위 for문을 정상적으로 실행완료했으면 else를 실행하라는 뜻
    print('done')

print('\n\n')

while False:
    print('...')

i=1
acc=0
while acc < 1000:
    acc += i
    i +=1
print(acc, i) # 자연수 1~45의 합이 1035

print('\n\n')

i=1
acc=0
while acc < 1000:
    acc += i
    i +=1
else: # while의 else
    acc -= (i-1)
print(acc, i) # 자연수 덧셈중 1000미만의 합
