a,b = eval(input("输入两个整数用逗号隔开: "))
t=1
if a<b:
    for i in range(1,a+1):
        if (a % i)==0 and  (b % i)==0:
            t=i
else:
    for i in range(1,b+1):
        if (a % i)==0  and (b % i)==0:
            t=i
print("最大公约数为：{}\n最小公倍数为：{}".format(t,a*b/t))
