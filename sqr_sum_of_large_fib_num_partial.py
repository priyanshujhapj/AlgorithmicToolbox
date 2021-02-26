def pisanoModulo(n):
    m = n+1
    remainder = n%60

    previous, current = 0, 1
    if remainder==0:
        return 0
    elif remainder==1:
        return 1
    for i in range(remainder-1):
        previous, current = current, (previous+current)

    N = current%10

    remainder = m%60
    previous, current = 0, 1
    if remainder==0:
        return 0
    elif remainder==1:
        return 1
    for i in range(remainder-1):
        previous, current = current, (previous+current)

    M = current%10

    return (N*M)%10

print(pisanoModulo(int(input())))