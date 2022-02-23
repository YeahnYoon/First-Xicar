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