# n = input()
# m = input()

# n = int(n)
# m = int(m)

# print(abs(n-m))
# print(a-b)
# print(a*b)


# if a > b : 
#     print(">")
# elif a < b : 
#     print("<")
# else : 
#     print("==")

# a, b = map(int, input().split())
# print(abs(a-b))

a, b, c, d, e = map(int, input().split())
x_1 = [a, b, c, d, e]
x = 0


for i in x_1 :  
    x += i ** 2

x%=10
print(x)

# 2744 부터
