"""
任务：给定了一个 Dog 类，类中有 foot、weight 和 height 三个属性。请在类的外部输出这三个属性的值。
"""

class Animal:
    foot = 4
    weight = 14
    height = 30

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
# 第1步：实例化类
a=Animal()
# 第2步：输出三个类属性的值
print("foot属性值为：%d"%a.foot)
print("weight属性值为：%dkg"%a.weight)
print("height属性值为：%dcm"%a.height)
########## End ##########
