a, b = input().split()

a, b = int(a), int(b)

def gcd(a, b):

    if b==0:
        return a

    r = a%b
    return gcd(b, r)

def lcm(a, b):
    return int((a/gcd(a,b))*b)

print(lcm(a,b))
