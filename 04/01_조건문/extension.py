import os
from unittest import result

filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']
result=[]
for filename in filenames:
    #print(filename,filename.split('.')[-1])
    extension = filename.split('.')[-1]
    if extension == 'h' or extension == 'c':
        result.append(filename)
print(result)