
'''
def demo(obj=[]):  #定义函数并为参数obj指定默认值
    print("obj值: ",obj)
    obj.append(1)

demo()

demo()
demo()
'''

def demo(obj=None):  #定义函数并为参数obj指定默认值
    if obj==None:
        obj = []
    print("obj值: ",obj)
    obj.append(1)
demo()
demo()
