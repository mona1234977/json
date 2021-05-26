# def hello( x,y):
#     print(a)
# hello(12)



# import itertools
# for i in itertools.count():
#     print(i)

# n=0
# list=[0]
# for i in list:
#     n=n+1
#     list.append(n)
#     print(list)                                                 



s =[12,42,70304,8756,22]
a=int(input("enter the number"))
b=str(a)
l=len(b)
t=l-1
i=0
while i<len(b):
    c=int(b[i])
    num=(c)*10**t
    print(num,end=" ")
    if i!=len(b)-1:
        print("+",end=" ")
    i=i+1
    t=t-1