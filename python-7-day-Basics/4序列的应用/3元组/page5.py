import random
randomnumber = (random.randint(10,100) for i in range(10))
print(randomnumber)


randomnumber1 = (random.randint(10,100) for i in range(10))
randomnumber1 = tuple(randomnumber1)  #转换为元组
print(randomnumber1)

print('-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

number = (i for i in range(3))
print(number.__next__()) #输出第1个元素
print(number.__next__()) #输出第2个元素
print(number.__next__()) #输出第3个元素
number = tuple(number)  #转换为元组
print("转换后：",number)

number = (i for i in range(3))   #生成生成器对象
for i in number:   #遍历生成器对象
    print(i,end=" ")  #输出每个元素的值
print(tuple(number))  #转换为元组输出
