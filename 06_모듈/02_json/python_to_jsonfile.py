import json

data = {"ciry": "Busan", "population": 3249975}
fd = open('busan.json', "w", encoding="utf-8")
json.dump(data, fd, indent=2, ensure_ascii=False)
fd.close()

print(open('busan.json').read())
