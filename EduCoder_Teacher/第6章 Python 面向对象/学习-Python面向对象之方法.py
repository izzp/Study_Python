"""
任务：给定一段代码，请修改其中部分代码，使代码可以成功运行。
"""


# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########## Begin ##########
class Kls:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def checkind():
        return IND == 'ON'

    def do_reset(self):
        if self.checkind():
            print('输入的值为 %s' % self.data)

IND = 'ON'
k = Kls(input())
k.do_reset()
########## End ##########


