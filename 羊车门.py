from random import *
car = randint(1,3)
user = eval(input("用户的选择: "))
trueno = 0
trueyes = 0
falseno = 0
falseyes = 0
g = []
for i in [1,2,3]:
    if i != car:
        g.append(i)#append用于给g添加对象,添加的对象不包括car
for i in g:
    if user != i:
        door = i
for i in [1,2,3]:
    if i != door and i != car:
        goat = i
print("user:{},door open:{}".format(user,door))
choice = input("你想改变你的选择吗？（yes or no）: ")
if choice == 'no':
    if user == car:
        trueno += 1
    else:
        falseno += 1
else:
    for i in [1,2,3]:
        if i !=user and i !=door:
            user=i
            break
    if user == car:
        trueyes += 1
    else:
        falseyes += 1
print("choice is : {}, guess {}".format(choice,'yes' if trueno == 1 or trueyes == 1 else 'no' ))
print("user:{},car:{},door open:{}".format(user,car,door))
        
