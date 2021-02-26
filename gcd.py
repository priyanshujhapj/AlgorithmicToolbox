
a, b = input().split()

a,b = int(a), int(b)

def EuclidGCD(a,b):
    if b==0:
        return a
    r = a%b
    return EuclidGCD(b,r)

print(EuclidGCD(a, b))