import json

fd = open("seoul.json", "r")
data = json.load(fd)
print(data)
fd.close()