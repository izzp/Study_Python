"""
任务：给定一个字典，该字典的值只能是整型数据，键为该数字的字符型，比如`{"5":5}`。
但是字典中的键值对并不是都按照这个规则排序的，可能出现`{"5":4}`的情况，请编写代码将字典的值改为和键一致的整型数值。
例如：{"5":4,"3":2}改为{"5":5,"3":3}
"""

dict1 = {"4":3,"14":14,"5":6,"33":33,"25":25,"18":68,"0":0,"10":3,"42":24,"7":1,"64":64,"49":49,"90":90,"48":48,"68":86,"41":12,"46":46,"91":91,"75":75,"27":39,"34":3,"57":11}

# 请在下面的Begin-End之间按照注释中给出的提示编写正确的代码
##########Begin##########
# 请编写代码实现任务要求，打印更改后的字典
for key,value in dict1.items():
    dict1.update({key:int(key)})
print(dict1)
##########End##########
