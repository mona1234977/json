import json

data={"name": "David",
   "class":"I",
   "age": 6}

file = open("que2.json","r+")
n=json.load(file)
print(n)
file.close()