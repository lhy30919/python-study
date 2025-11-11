import csv

# 읽기
rows = []
with open("test.csv", newline='') as fd:
    reader = csv.reader(fd)
    for row in reader:
        if row[0] == '2':
            row[2] = 'pass1.'
        rows.append(row)

# 쓰기
with open("test2.csv", "w", newline='') as fd:
    writer = csv.writer(fd)
    writer.writerows(rows)
