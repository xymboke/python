def division():
    ''' 功能:分苹果 '''
    print("\n","="*20,"蚂蚁庄园动态","="*20)
    apple = int(input("请输入苹果的个数: "))   #输入苹果的数量
    children = int(input("请输入来了几个小朋友: "))
    result = apple//children     #计算每个人分几个苹果
    remain = apple-result*children  #计算余下几个苹果
    if remain>0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,
              "个，剩下",remain,"个。")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个。")

if __name__=="__main__":
    try:                      #捕获异常
        division()            #调用分苹果的函数
    except ZeroDivisionError:  #处理异常
        print("\n出错了 ~-~ --苹果不能被0个小朋友分!")
