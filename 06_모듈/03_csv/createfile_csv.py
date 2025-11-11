import os

data = """id,name,pass
1,lee,soldesk1.
2,kim,soldesk2.
3,park,soldesk3."""

# 파일 생성
file1 = 'test.csv'
with open(file1, "w") as fd:
    fd.write(data)

# 파일 읽기 및 수정
output_data = []
with open("test.csv") as fd:
    for line in fd:
        cols = line.strip().split(',')
        if cols[0] == '2':
            cols[2] = 'pass1.'  # 비밀번호 수정
        output_data.append(cols)

# 수정된 내용 다시 쓰기
file2 = 'test2.csv'
with open(file2, "w") as fd:
    for row in output_data:
        fd.write(','.join(row) + '\n')

print("[  OK  ] 변경된 CSV 파일이 저장되었습니다.")
