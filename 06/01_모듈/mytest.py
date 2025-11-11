# import mymodule		# mymodule.py 파일을 사용하겠다.
# print(mymodule.person["age"])

from mymodule import person # mymodule.py 파일의 person만 사용하겠다.

a = person["age"]		# mymodule.py 파일에 person 객체
print(a)

# from mymodule import *
# print(person["age"])