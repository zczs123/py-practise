for i in range(21):
    if i%5 == 0:
        for j in range(21):
            if j%5 == 0:
                print("+",end='')
            else:
                print("-",end='')
        print("\n")
    else:
        for k in range(21):
            if k%5 == 0:
                print("i",end='')
            else:
                print(" ",end='')
        print("\n")
