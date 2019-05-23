import re
pattern = r'[?|&]'  #定义分割符
url='http://www.baidu.com/login.jsp?uername="mr"&pwd="mrsoft"'
result=re.split(pattern,url)  #分割字符串
print(result)
