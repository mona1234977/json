import json
def is_complex_num(objects):
    if "complex" in objects:
        return complex(objects["real"],objects["img"])
    return objects
complex_object=json.loads('{"real":4,"img":5}')
print(is_complex_num(complex_object))