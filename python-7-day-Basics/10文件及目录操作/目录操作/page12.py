'''
os模块的walk()函数用于实现遍历目录的功能


'''
import os
#遍历目录
tuples = os.walk("H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作")

for tuple1 in tuples:   #通过for循环输出遍历结果
    print(tuple1,"\n")  #输出每一级目录的元组
