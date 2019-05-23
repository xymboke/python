char = ['cat','Tom','Angela','pet']
char.sort()  #默认区分字母大小
print("区分字母大小写: ",char)
char.sort(key=str.lower)#不区分字母大小写
print("不区分字母大小写:",char)



print("========================================")
grade = [545,88,86,21,23,33,1,3,65,6]
grade_as = sorted(grade) #进行升序排列
print("升序",grade_as)
grade_des = sorted(grade,reverse=True) #进行降序排列
print("升序",grade_as)
print("原序列：",grade)

print("========================================")
import random
randomnumber = [random.randint(10,100) for i in range(10)]
print("生成随机数为: ",randomnumber)
print("========================================")
price = [1200,5330,2988,6200,1998,8888]
sale = [int(x*0.5) for x in price]
print("原价格：",price)
print("打五折的价格：",sale)
print("========================================")
sale1=[x for x in price if x>5000]
print("原价格：",price)
print("价格：",sale1)
