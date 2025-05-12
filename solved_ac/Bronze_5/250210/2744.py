# https://www.acmicpc.net/problem/2744
a = str(input())
#a = "WrongAnswer"
b = ""
for i in a : 
    if i == i.upper() : 
        i = i.lower() # b.append()        
        b+=i
    else : 
        i = i.upper()
        b+=i
print(b)
