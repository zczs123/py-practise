def isNum(num):    
    try:
        t=type(eval(num))
        if t==int or t==float or t==complex:
            return True
    except ValueError:
        return False
    except NameError:
        return False
num=isNum(input("输入要判断的数："))
print(num)         
            
