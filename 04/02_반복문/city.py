#!/usr/bin/python3

#Long Name City : suncheon
#Short Name City : seoul, kimpo, pusan

def char_len_search(ilist):
    # input  : list(ilist)
    # output : list(olist)
    olist=[]
    for item in ilist:
        olist.append(len(item))

    return olist

def max_min_len_list(ilist):
    # input  : list(ilist)
    # output : int(max), int(min)
    # function : [5,6,4,8,5] => 8, 5
    return max(ilist), min(ilist)

def long_short_list(ilist,xlen,ylen):
    # input  : list(ilist), xlen(8), ylen(5)
    # output : [...], [...]
    long_list = []
    short_list = []
    for item in ilist:
        if len(item) == xlen:
            long_list.append(item)
        elif len(item) == ylen:
            short_list.append(item)
    return long_list, short_list

def transform(long_list, short_list):
    # input  : [], []
    # output : str1, str2

    print(f"{'Long Name City':<16}: {''.join(long_list)}")
    print(f"{'Short Name City':<16}: {', '.join(short_list)}")
def main():
    cities = ['seoul', 'daejeon', 'kimpo', 'suncheon', 'pusan']

    # 각 도시 이름의 길이 리스트
    cities_list = char_len_search(cities)

    # 최장/최단 길이 구하기
    maxlen, minlen = max_min_len_list(cities_list)

    # 길이에 따라 분류
    longest,shortest = long_short_list(cities, maxlen, minlen)

    # 출력
    transform(longest,shortest)

if __name__ == '__main__':
    main()