temstr=input("请输入带有符号的温度值：")
if temstr[-1] in ['F','f']:
    C=(eval(temstr[0:-1]) -32)/1.8
    print("转换后的温度是{:.2f}C".format(C))

elif temstr[-1] in ['C','c']:
       F=1.8*eval(temstr[0:-1]) + 32
       print("转换后的温度是{:.2f}F".format(F))
    
else:
       print("YOU ARE WRONG")
       
