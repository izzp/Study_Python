"""
任务：定义一个 Math 类，在类中定义一个 mean 方法，传入的参数为一个列表，该方法的作用是计算列表内所有元素的平均值。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 定义 Math 类，并在类中定义 mean 方法
class Math:
    def mean(self, list1):
        self.list1 = list1
        num = 0
        for x in self.list1:
            num += x
        return num / len(list1)


########## End ##########
# 实例化类
x = Math()
list1 = eval(input())
print("平均值为", x.mean(list1))
