n, m = input().split()
n, m = int(n), int(m)

def Pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m*m):
        previous, current = current, (current+previous)%m
        if (previous==0 and current==1):
            return i+1


def pisanoModulo(n, m):
    lperiod = Pisano_period(m)
    remainder = n%lperiod

    previous, current = 0, 1
    if remainder==0:
        return 0
    elif remainder==1:
        return 1
    for i in range(remainder-1):
        previous, current = current, (previous+current)

    return current%m


print(pisanoModulo(n,m))