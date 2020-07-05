"""
18. Find a package in the Python standard library for dealing with
JSON. Import the library module and inspect the attributes of the
module. Use the help function to learn more about how to use the
module. Serialize a dictionary mapping 'name' to your name and 'age'
to your age, to a JSON string. Deserialize the JSON back into
Python.
"""
import json
my_dict={"name":"Lalita Awasthi","age":23}
def to_json(dict):
    return json.dumps(dict)
def to_dict(json_of_dict):
    print(json.loads(json_of_dict))
json_of_dict=to_json(my_dict)
print(json_of_dict)
to_dict(json_of_dict)
