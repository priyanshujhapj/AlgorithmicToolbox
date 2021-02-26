n = int(input())

def fib_sum(n):

    if n==0:
        return 0
    if n==1:
        return 1

    n = n+2
    r = n%60
    pre, cur = 0, 1
    for i in range(r-1):
        pre, cur = cur, (pre+cur)

    cur = cur%10
    if (cur-1)<0:
        return 10+(cur-1)

    return cur-1

print(fib_sum(n))
