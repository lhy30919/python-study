j = "821010-1635210"
result=0
for i in range(2,8,1):
    result += int(j[i-2])*i
for i in range(2,6,1):
    result += int(j[i+7])*i

result %=11

result = 11-result

print(f'주민등록번호: {j}')
if j[-1]==result: print('유효하다')
else:print('유효하지 않다')