str = input("请输入一串字符串: ")
num , char , spa ,other = 0, 0 ,0 ,0
for i in str:
    if('a'<=i<='z' or 'A'<=i<='Z'):
        char += 1
    elif('0'<=i<='9'):
        num += 1
    elif i==' ':
        spa += 1
    else:
        other += 1
print("数字个数为：{}\n字母个数为：{}\n空格个数为：{}\n其他类型的个数为{}"\
          .format(num,char,spa,other))
