import json
n = {"Name":"mona",
      "city":"nainital",
      "state":"uttarakhand"}

print(type(n))
k = json.dumps(n)
print(k)