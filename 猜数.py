from random import *
r = randint(0,9)
for i in range(10):
    g = eval(input("请输入您要猜的整数: "))
    if g>r:
        print("您输入大了，请重新输入！")
    elif g<r:
        print("您输入小了，请重新输入！")
    else:
        print("恭喜您！经过{}次后，您猜对了！".format(i))
        break
