class MyStatic:
    def reset(self):  # 파이썬에서 메소드 선언방식
        self.x = 0
        self.y = 0
a = MyStatic()
MyStatic.reset(a) # 클래스 메소드 
# a.reset() 인스턴스메소드
print('x 값 : ',a.x)
print('y 값 : ',a.y)



