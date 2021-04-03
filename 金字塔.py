print("方法一")
row=1
while row <=4:
    print(" " *(4-row) + "*"*(2*row-1)+" "*(4-row))
    row+= 1
print("方法二")
row=1
while row <=4:
    print(("*"*(2*row-1)).rjust(4+row-1," "))
    row+= 1

print("升级圣诞树")
def anycount(m):
    row=1
    while row<=m:
        print(("*"*(2*row-1)).rjust(m+row-1," "))
        row+=1
    for k in range(1,row - 1):
        print("*".rjust((m + row -1)//2," "))
anycount(10)
print("正倒三角")
row=1
while row <=4:
    print(("*"*(2*row-1)).rjust(5+row-1," "))
    row+= 1
for i in range(row , 0 , -1):
    print(("*"*(2*i-1)).rjust(5+i-1," "))

    
