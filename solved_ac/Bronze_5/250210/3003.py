a = [1, 1, 2, 2, 2, 8]
s = list(map(int, input().split()))
t = []

for ai, bi in zip(a, s):
    t.append(ai - bi)

for i in range(len(t)) :
    print(t[i], end=" ")
