print('去除字符串中的空格和特殊字符')

str1= ' https://www.baidu.com   \t\n\r '
print('原字符串str1: ' + str1 + '。')
print('字符串：' +str1.strip() + '。') #去除字符串首尾的空格和特殊字符
str2= '@时间段.@.'
print('原字符串str2: ' + str2 + '。')
print('字符串：' +str2.strip('@.') + '。') #去除字符串首尾的“@” “.”
