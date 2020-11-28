"""
任务：定义一个 Dog 类，在类中定义属性 name 和 age；在类外部可以修改该 name 和 age 的值，值通过 input 获取。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
class Dog:
    def __init__(self, name, age):
        self.age = age
        self.name = name


# 第一步：定义属性


name = input()
age = int(input())
# 第二步：实例化类，并将 name 和 age 作为参数传给类
D = Dog(name, age)
# 第三步：按照预期输出打印结果
print("Dog %s的年龄为%d岁" % (D.name , D.age))
########## End ##########
