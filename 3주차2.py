import turtle

t= turtle.Turtle('turtle') # 'turtle'을 다루는 turtle 객체를 t객체로 만듬

def drawPolygon(t, n, length): # N각형 그리는 함수
    if n>1 and length>10:
        for i in range(n):
            t.forward(length)
            t.left(360/n)

turtle.Turtle.drawPolygon = drawPolygon
t.drawPolygon(10, 50)

def add(a,b) :
    return a+b

print(add(2,3))
print(add('hi\t', 'hello'))
a, b = 2, 3
print(a+b) # 실제로  +가 정해져있지않음 a라는 객체안의 add 함수임
print(a.__add__(b)) # 정수형 객체에는 add는 숫자를 더하는것
s1, s2 = 'hi\t', 'hello'
print(s1.__add__(s2)) # 문자형 객체에는 add는 문자를 연결하는것
