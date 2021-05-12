import math
class Test:
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0,0)
    def calc_distance(self, other):
        return math.sqrt(
                (self.x - other.x)**2 +
                (self.y - other.y)**2  )


if __name__ == '__main__':

    t1  = Test()
    t2 = Test()
    t1.reset()
    t2.move(10,0)
    print('t1가 이동한 후 t2와 거리계산결과: {}'.format(t1.calc_distance(t2)))
    t2.move(10,0)
    print('t1이 이동한 후 t2와 거리계산결과: {}'.format(t1.calc_distance(t2)))
    t1.move(10, 0)
    print('t1이 이동한 후 t2과 거리계산결과: {}'.format(t1.calc_distance(t2)))

