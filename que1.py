import json

data={"Name":"Ram",
"Class":"IV",
"Age":9 }

file = open("que1.json","w")
json.dump(data,file)
file.close()