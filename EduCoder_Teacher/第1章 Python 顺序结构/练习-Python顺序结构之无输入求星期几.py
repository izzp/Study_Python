﻿"""程序代码
任务：已知 2018 年 1 月 1 号是星期一，2 月 15 日是除夕，余数为 0 表示星期日，余数为 1 表示星期一，余数为 2 表示星期二，以此类推。
"""

#请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
########### Begin ###########
#第1步：计算2月15日是2018年的第几天，赋值给变量day
day = 46
#第2步：用day的值和一周的天数进行取余运算，将余数赋值给week_day，即得到需要的星期结果
week_day = day % 7
#第3步：打印week_day的值
print(week_day)
########### End ###########