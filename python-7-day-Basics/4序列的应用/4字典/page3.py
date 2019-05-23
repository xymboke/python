dictionary = {'qq':'465','咖啡店':'56132','无语':'4568'}
for item in dictionary.items():
    print(item)

for key,value in dictionary.items():
    print(key,"的联系电话是",value)

print("-=-===================-----------------------------------------------")
dictionary = dict((('圣诞节','水瓶座'),('冷一','射手座'),('奥德赛','双鱼座'),('戴兰','双子座')))
dictionary['斯柯达'] = '巨蟹座'  #添加一个元素
print(dictionary)
print("-=-===================-----------------------------------------------")
dictionary['圣诞节'] = '巨蟹座'  #添加一个元素
print(dictionary)
print("-=-===================-----------------------------------------------")
dictionary = dict((('圣诞节','水瓶座'),('冷一','射手座'),('奥德赛','双鱼座'),('戴兰','双子座')))
del dictionary['圣诞节']
print(dictionary)


del dictionary['上登录放假']
print(dictionary)
