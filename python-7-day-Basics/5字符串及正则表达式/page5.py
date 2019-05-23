str1='@斯柯达 @数据库 @代付款'
print('字符串“',str1,'”中包括',str1.count('@'),'个@符号')

print("*="*40)

print('字符串“',str1,'”中@符号首次出现的位置索引为: ',str1.find('@'))
print("*="*40)
print('字符串“',str1,'”中@符号首次出现的位置索引为: ',str1.find('*'))
print('@' in str1)


print("*="*40)
print('字符串“',str1,'”中@符号首次出现的位置索引为: ',str1.index('@'))
print("*="*40)
print('字符串“',str1,'”中@符号首次出现的位置索引为: ',str1.rindex('@'))#从右边开始查询
#print('字符串“',str1,'”中@符号首次出现的位置索引为: ',str1.index('*'))


print('检索开头')
print('判断字符串“',str1,'”是否以@符号开头，结果为: ',str1.startswith('@'))


str2='https://www.baidu.com'
print('判断字符串“',str2,'”是否以.com结尾，结果为: ',str2.endswith('.com'))
str3='WWW.Baidu.com'
print('原字符串：',str3)
print('新字符串：',str3.lower()) #全部转换为小写字母输出
print('新字符串：',str3.upper()) #全部转换为大写字母输出
