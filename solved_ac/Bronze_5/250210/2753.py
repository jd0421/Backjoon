# https://www.acmicpc.net/problem/2753
A = int(input())

if A%4 == 0 and A%100 != 0 :
    print("1") # 윤년
else :
    if A%400 == 0 : 
        print("1") # 윤년
    else : 
        print("0") # 윤년 아닐 경우
        