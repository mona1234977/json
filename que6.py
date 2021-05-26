import json
python_object = '{"a": 1, "a": 2, "a": 3, "a": 4, "b": 4, "b": 2}'
print("original python object")
print(python_object)
json_object = json.loads(python_object)
print("unique key in a Json object:")
print(json_object)