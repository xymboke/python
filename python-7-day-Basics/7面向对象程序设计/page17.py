class Fruit:     #定义水果类（基类）
    def __init__(self,color="绿色"):
        Fruit.color=color     #定义类属性
    def harvest(self):
        print("水果原来是："+Fruit.color+"的!")  #输出的是类属性color
class Apple(Fruit):                              #定义苹果类（派生类）
    def __init__(self):
        print("我是苹果")
        super().__init__() #调用基类的__init__()方法
apple=Apple()        #创建类的实例（苹果）
apple.harvest()      #调用基类的harvest()方法
