'''
使用rmdir()函数只能删除空的目录，如果想要删除非空目录，则需要使用python
内置的标准模块shutil的rmtree()函数实现。

'''

import shutil
#删除目录下的asd子目录及其内容
shutil.rmtree("H:\\资料总整理\\python\\10基础\\10 文件及目录操作\\目录操作\\exe\\asd")
