verse = '野渡无人舟自横'
byte=verse.encode('GBK')  #采用GBK编码转换为二进制数据，不处理异常
print('原字符串：',verse) #输出原字符串（没有改变）
print('转换后：',byte)  #输出转换后的二进制数据
byte1=verse.encode('utf-8')  #采用GBK编码转换为二进制数据，不处理异常
print('转换后：',byte1)  #输出转换后的二进制数据

print('解码后：',byte.decode("GBK")) #对进行制数据进行解码
print('解码后：',byte1.decode("utf-8")) #对进行制数据进行解码
