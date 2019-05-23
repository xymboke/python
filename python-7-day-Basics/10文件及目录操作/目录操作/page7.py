import os
def mkdir(path):                       #定义递归创建目录的函数
    if not os.path.isdir(path):        #判断是否为有效路径
        mkdir(os.path.split(path)[0])  #递归调用
    else:                              #如果目录存在，直接返回
        return
    os.mkdir(path)                  #创建目录
mkdir("H:/资料总整理/python/10基础/10 文件及目录操作/目录操作/e")
