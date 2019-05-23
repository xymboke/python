import re

pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'  #模式字符串
about = '我是一名程序员，我喜欢看黑客方面的图书，想研究下Trojan。\n'
sub = re.sub(pattern,'@_@',about)  #进行模式替换
print(sub)
about = '我是一名程序员，我喜欢看黑客方面的图书，想研究下Trojan'
sub = re.sub(pattern,'@_@',about)  #进行模式替换
print(sub)
