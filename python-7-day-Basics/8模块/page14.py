import random

if __name__=='__main__':
    checkcode=""  #保存验证码的变量
    for i in range(4):    #循环4次
        index=random.randrange(0,4)  #生成0到3中的一个数
        if index != i and index + 1 != i:
            checkcode += chr(random.randint(97,122))   #生成a到z中的一个小写字母
        elif index + 1 == i :
            checkcode += chr(random.randint(65,90))   #生成A到Z中的一个大写字母
        else:
            checkcode += str(random.randint(1,9))  #生成1到9中的一个数字
    print("验证码: ",checkcode)     #输出生成的验证码
