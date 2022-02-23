#####################################################################
car_maker = ["Hyundai","BMW",'Benz']

if "Hyundaiㅁ" in car_maker: print("현대")
else: print("현대를 뺴먹지 말자 ㅋㅋ")

print("111")

for i in range(0,11):
    print(i)

#####################################################################
list_1 = ["Hyundai","BMW",'Benz']

for i in list_1:
    print(i)

a=[(1,2),(3,4),(5,6)]

for (x,y) in a:
    print(x+y)

for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)
#####################################################################
# 예외 처리(Fail-Safe)
try:
    #실행
    a = [1, 2]
    print(a[3])
except IndexError as e:
    #에러 발생시 진행할 일
    print(e)
    print("에러가 발생했어~~")
    print("1,2는 살아있어~~")
finally:
    #최종적으로 진행할 일
    print(a[:])
#####################################################################
# 클래스 관리

class my_class:
    # 초기화 객체
    def __init__(self,x,y):
        self.data = x
        self.data2 = y

    def myfunc(self):
        print("myfunc")
        self.data = 3

class your_class:
    data = 0

a = my_class(10,5)
b = my_class(10,6)
c = your_class()

a.myfunc()

print(a.data)
print(b.data)
print(c.data)
#####################################################################
# 클래스 상속
class my_class:
    # 초기화 객체
    def __init__(self):
        self.data = 5
        self.data2 = 10

    def myfunc(self):
        print("myfunc")
        self.data = 3

class your_class(my_class):
    data_3 = 20

a = my_class()
b = my_class()
c = your_class()

a.myfunc()
c.myfunc()

print(a.data)
print(b.data)
print(c.data)
print(c.data_3)
#####################################################################
# 모듈
class my_class:
    # 초기화 객체
    def __init__(self):
        self.data = 5
        self.data2 = 10

    def myfunc(self):
        print("myfunc")
        self.data = 3

class your_class(my_class):
    data_3 = 20

if __name__ == '__main__':

    a = my_class()
    b = my_class()
    c = your_class()

    a.myfunc()
    c.myfunc()

    print(a.data)
    print(b.data)
    print(c.data)
    print(c.data_3)