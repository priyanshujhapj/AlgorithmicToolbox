n = int(input())
a = input().split()
b = input().split()

a = [int(i) for i in a]
b = [int(j) for j in b]

result = 0

for i in range(n):
    A = max(a)
    B = max(b)
    n = A*B
    result+=n
    a.remove(A)
    b.remove(B)

print(result)