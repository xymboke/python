template = '编号：%09d\t公司名称：%s \t官网：http://www.%s.com'  #定义模板
context1=(7,'百度','baidu')   #定义要转换的内容1
context2=(8,'撒娇','sajiao')   #定义要转换的内容2
print(template%context1)  #格式化输出
print(template%context2)  #格式化输出


template1 = '编号：{:0>9s}\t公司名称：{:s} \t官网：http://www.{:s}.com'  #定义模板
context3=template1.format('7','百度','baidu')   #定义要转换的内容1
context4=template1.format('8','撒娇','sajiao')   #定义要转换的内容2
print(context3)  #格式化输出
print(context4)  #格式化输出
