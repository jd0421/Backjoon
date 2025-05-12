# range 에 변화를 주는 방법
A = int(input())

for i in range(A) :
	print("*"* (i+1))
	
# 변수 자체에 변화를 주는 방법

a = int(input())

for i in range(1, a+1) : 
    print(i * "*")