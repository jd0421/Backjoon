# 풀이 1
a, b, c, d, e = map(int, input().split())
x_1 = [a, b, c, d, e]
x = 0

for i in x_1 :  
    x += i ** 2

x%=10
print(x)

# 풀이 2

# 입력
a = input().split() 

# 검증수
b = 0 

for i in range(len(a)) :
    b+= (int(a[i])**2)

b%=10
print(b)

