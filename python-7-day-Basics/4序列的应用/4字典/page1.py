dictionary = {'qq':'465','咖啡店':'56132','无语':'4568'}
print(dictionary)

name = ['佛冈','东风','阿莎','赛罗']  #作为键的列表
sign = ['水瓶座','射手座','双鱼座','双子座'] #作为值的列表
dictionary = dict(zip(name,sign)) #转换为字典
print(dictionary) #输出转换后字典

print(dictionary['东风'])
print('爱仕达星座是：',dictionary['视角'] if '视角' in dictionary else '我的字典里没有此人')
print('佛冈星座是：',dictionary['佛冈'] if '佛冈' in dictionary else '我的字典里没有此人')
print("阿莎的星座是：",dictionary.get('阿莎'))


print('-=---------------=----------------------=')
dictionary1 = dict(绮梦='水瓶座',冷一='射手座',香凝='双鱼座',戴兰='双子座')
print(dictionary1)

print('-=---------------=----------------------=')
name_list = ['佛冈','东风','阿莎','赛罗']   #作为键的列表
dictionary2=dict.fromkeys(name_list)
print(dictionary2)

print('-=---------------=----------------------=')
name_list1 = ('佛冈','东风','阿莎','赛罗')   #作为键的元组
sign1 = ['水瓶座','射手座','双鱼座','双子座'] #作为值的列表
dictionary3={name_list1:sign1}
print(dictionary3)


print('-=---------------=----------------------=')
name_list2 = ['佛冈','东风','阿莎','赛罗']   #作为键的列表
sign2 = ['水瓶座','射手座','双鱼座','双子座'] #作为值的列表
dictionary4={name_list2:sign2}
print(dictionary4)

