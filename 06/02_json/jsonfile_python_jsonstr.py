import json

fd = open("seoul.json", "r")
data = json.load(fd)
print(data)
fd.close()

data["population"] = 9600000
data["gu"] = 25
print(data)

json_str = json.dumps(data)
print(json_str)
