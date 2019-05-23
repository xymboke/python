height= 1.7
print("您的身高：" + str(height))
weight = 48.5
print("您的体重：" + str(weight))
bmi = weight/(height*height)  #计算BMI指数
print("您的BMI指数为：",str(bmi))


#判断身材是否合理
if bmi <18.5:
    print("您的BMI指数为：",str(bmi))
    print("您的体重过轻 ~@_@~\n")
if bmi>=18.5 and bmi<24.9:
    print("您的BMI指数为：",str(bmi))
    print("正常范围，注意保持（-_-）\n")
if bmi>=24.9 and bmi<29.9:
    print("您的BMI指数为：",str(bmi))
    print("您的体重过重 ~@_@~\n")
if bmi>=29.9:
    print("您的BMI指数为：",str(bmi))
    print("肥胖 ~@_@~\n")
