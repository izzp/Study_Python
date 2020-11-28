"""
任务：定义一个 Cuboid 类，该类有长、宽和高三个属性，而且类中定义了一个求表面积的函数 area 和 体积函数 volume，
长、宽和高都是通过 input 函数获取，请编写代码实现该类。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 第一步：定义Cuboid类，定义长、宽和高三个属性
class Cuboid:
    def __init__(self, length, wigh, high):
        self.length = length
        self.wigh = wigh
        self.high = high
# 第二步：在类中定义area函数和volume函数
    def area(self):
        return 2 * (self.length * self.wigh + self.length * self.high + self.wigh * self.high)
    def volume(self):
        return self.length * self.wigh * self.high


# 第三步：实例化类，并调用函数
a = int(input())
b = int(input())
c = int(input())
C = Cuboid(a, b, c)
area = C.area()
volume = C.volume()
print("表面积为%d平方米" % area)
print("体积为%d立方米" % volume)
########## End ##########
