sum, orgin = 0, 100
for i in range(1,11):
    sum=sum+orgin
    orgin=orgin/2
    sum=sum+orgin
print("共经过{}米，第十次反弹{}米".format(sum,orgin))
