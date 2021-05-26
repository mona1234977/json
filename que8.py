import json

list1=["neelam","programer","24","24000"]
list2=["komal","trainer","24","200000"]
list3=["anuradha","HR","25","400000"]
list4=["Abhishek","manager","29","630000"]
keys=["name","designation","age","salary"]
emp1={}
emp2={}
emp3={}
emp4={}
dic1={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}
for i in range(len(list1)):
    emp1.update({keys[i]:list1[i]})
for j in range(len(list2)):
    emp2.update({keys[j]:list2[j]})
for s in range (len(list3)):
    emp3.update({keys[s]:list3[s]})
for a in range(len(list4)):
    emp4.update({keys[a]:list4[a]})
with open("MONA.json","w") as g:
    json.dump(dic1,g,indent=2)
with open("MONA.json","r") as g:
    d=json.load(dic1)
    print(d)