print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
for number in range(100):
    if number%3 == 2 and number%5 == 3 and number%7 == 2: #判断是否符合条件
        print("答曰：这个数是",number)  #输出符合条件的数


string = '不要再说我不能'
print(string)  #横向显示
for ch in string:
    print(ch)  #纵向显示
