import json

json_read = open("json2.txt", "r")
a=json.load(json_read)
print(a[0])