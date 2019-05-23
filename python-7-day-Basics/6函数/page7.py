def printcoffee(*coffeename):
    print('\n我喜欢的咖啡有:')
    for item in coffeename:
        print(item)

printcoffee('蓝山')
printcoffee('蓝山','卡布奇若','土耳其','巴西','哥伦比亚')
printcoffee('蓝山','卡布奇若','曼特宁','摩卡')

print('======================================')

param = ['蓝山','卡布奇若','土耳其']
printcoffee(*param)
