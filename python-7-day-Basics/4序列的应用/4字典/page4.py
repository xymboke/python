dictionary = dict((('圣诞节','水瓶座'),('冷一','射手座'),('奥德赛','双鱼座'),('戴兰','双子座')))
if '斯柯达' in dictionary: #如果存在
    del dictionary['斯柯达']
print(dictionary)

print("-=-===================-----------------------------------------------")
import random
randomdict = {i:random.randint(10,100) for i in range(1,5)}
print("生成的字典为：",randomdict)


print("-=-===================-----------------------------------------------")

name = ['佛冈','东风','阿莎','赛罗']  #作为键的列表
sign = ['水瓶座','射手座','双鱼座','双子座'] #作为值的列表
dictionary = {i:j+'座' for i,j in zip(name,sign)}  #使用列表推到式生成字典
print(dictionary)
