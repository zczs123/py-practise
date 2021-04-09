def isPrime(num):
    try:
        if num==0 or num==1:
            return False
            c=0
            for i in range(1,k+1):
              if k%i==0:
                c += 1
            if c>2:
                return False
            else:
                return True
        else:
            return False
    except ValueError:
        return False
num=isPrime(input("输入一个整数："))
print(num)
            
