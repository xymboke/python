import page5 as r  #导入矩形模块
import page6 as c   #导入圆形模块

if __name__=='__main__':
    print("圆形的周长为：",c.girth(10))      #调用计算圆形周长的函数
    print("矩形的周长为：",r.girth(10,10))   #调用计算矩形周长的函数
