import os

data     = """
반갑습니다. 
python 개발자 여러분 한살 더 드셨죠!
올 한해는... 행복한 가득한 한해가 되었으면 합니다.
06/03_csv/createfile.py 에서 생성됨
"""

dirname  ='../../test'
filename =f'{dirname}/test.txt'

# print(os.getcwd()) # 현재 경로 출력
if os.path.isdir(dirname) == False:    # 디렉터리 생성
    os.mkdir(dirname)

# 파일 생성
if os.path.isfile(filename) == False : # 파일 생성
    filename  = f'{filename}'
    fd        = open(filename, 'w')
    fd.write(data)                     # 파일 수정
    fd.close()                         # 파일 닫기
# 파일 확인
print(open(filename).read())
# 파일 삭제
# if os.path.isfile(filename) == True :
#     os.remove(filename)