m, n = input().split()
m, n = int(m), int(n)

def sum_fib(m,n):

    m = m+2
    r = m%60
    pre, cur = 0, 1
    for i in range(r-1):
        pre, cur = cur, (pre+cur)
    M = cur%10
    M = M-1

    n = n+2
    r = n%60
    pre, cur = 0, 1
    for i in range(r-1):
        pre, cur = cur, (pre+cur)
    N = cur%10
    N = N-1

    final = (N-M)%10

    return final

print(sum_fib(m-1,n))