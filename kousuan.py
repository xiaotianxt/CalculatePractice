NUMBER = 25
import random
import csv
import pandas

def plus(adigit,bdigit):
    asklist=[[random.randint(10**(bdigit-1),10**adigit),random.randint(10**(bdigit-1),10**bdigit)] for i in range(NUMBER)]
    anslist=[str(asklist[i][0]+asklist[i][1]) for i in range(NUMBER)]
    asklist = [str(asklist[i][0])+' + '+str(asklist[i][1]) for i in range(NUMBER)]
    return asklist,anslist

def minus(adigit,bdigit):
    asklist=[[random.randint(10**(adigit-1),10**(adigit)), random.randint(10**(bdigit-1),10**bdigit)] for i in range(NUMBER)]
    for i in range(NUMBER):
        if asklist[i][0]<asklist[i][1]:
            asklist[i][0],asklist[i][1] = asklist[i][1],asklist[i][0]
        else:
            pass
    anslist=[str(asklist[i][0]-asklist[i][1]) for i in range(NUMBER)]
    asklist = [str(asklist[i][0])+' - '+str(asklist[i][1]) for i in range(NUMBER)]
    return asklist,anslist

def multiply(adigit,bdigit):
    asklist=[]
    anslist=[]
    for i in range(NUMBER):
        a,b = random.randint(10,99),random.randint(10,99)
        asklist.append(str(a)+' × '+str(b))
        anslist.append(str(a*b))
    return asklist,anslist

def divide(adigit,bdigit):
    asklist=[]
    anslist=[]
    for i in range(NUMBER):
        a,b = random.randint(100,1000),random.randint(10,100)
        asklist.append(str(a) + ' ÷ ' + str(b))
        anslist.append(str(a//b)+' …… '+ str(a-a//b*b))
    return asklist,anslist

funclist=[plus,minus,multiply,divide]

Final=[]
for fun in funclist:
    a,b = fun(3,3)
    for i in range(NUMBER):
        Final.append([a[i],b[i]])

name = ['ask','ans']
test = pandas.DataFrame(data=Final)
print(test)
test.to_csv('nbnb.csv',encoding='gbk')



