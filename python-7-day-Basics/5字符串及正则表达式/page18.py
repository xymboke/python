import re
pattern = r'1[34567]\d{9}'  #定义要替换的模式字符串
string = '中奖号码为：84978981 联系电话：13611112222'
result=re.sub(pattern,'1xxxxxxxxxx',string)  #替换字符串
print(result)
