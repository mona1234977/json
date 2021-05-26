import json
k ={"4":5,
    "6":7,
    "1":3,
    "2":4}
file = open("que4.json","w")
n=json.dump(k,file,sort_keys=True,indent=2)
file.close()