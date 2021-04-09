def multi(*num):
    if not all(num):
        return 0
    else:
        mul=1
        for i in  num:
            mul=mul*i
        return mul
print(multi(1,2,3))
    
