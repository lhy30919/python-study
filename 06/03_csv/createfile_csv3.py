import pandas as pd

# CSV 파일 읽기
df = pd.read_csv("test.csv")
print("원본 데이터:")
print(df, "\n")

# 데이터 수정
df.loc[df["id"] == 2, " pass"] = " pass1."   # id=2 행의 pass 열 변경

# 수정된 내용 확인
print("수정된 데이터:")
print(df, "\n")

# 새 파일로 저장
df.to_csv("test2.csv", index=False)
print("변경된 CSV 파일이 test2.csv 로 저장되었습니다.")
