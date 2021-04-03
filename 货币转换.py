t=input("输入要转换的货币值及其单位：")
if t[-1] in ['元']:
    dollor = (eval(t[0:-1]))/6
    print("转换后为美元为{:.2f}$".format(dollor))
if t[-1] in ['$']:
    RMB=(eval(t[0:-1]))*6
    print("转换后为人民币为{:.2f}RMB".format(RMB ))
else:
