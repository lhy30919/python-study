# 파이썬에서 파일 읽기
import json

fd = open('seoul.json', "r", encoding="utf-8")
data = json.load(fd)
print(data)

data["population"] = 9600000
print(data)

fd.close()

