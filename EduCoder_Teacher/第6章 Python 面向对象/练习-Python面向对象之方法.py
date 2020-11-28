import math

R = int(input())  # 获取球的半径


class Sphere:
    # 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
    ########## Begin ##########
    # 第1步：定义构造函数
    def __init__(self, R):
        self.pi = math.pi
        self.r = R

    # 第2步：定义volumn方法求球的体积
    def volumn(self):
        return (self.r ** 3) * self.pi * (4 / 3)


# 第3步：实例化类，调用volumn方法求体积，打印球的体积
s = Sphere(R)
print("体积为%s立方米" % s.volumn())
########## End ##########
