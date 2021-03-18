distance = int(input())
L = int(input())
no_gas_st = int(input())
x = input().split()
x = [int(i) for i in x]
x.insert(0, 0)
x.insert(len(x), distance)
n = len(x)-1

def min_refills(x,n,L):
    cur_refill = 0
    num_refill = 0
    while cur_refill<n:
        last_refill = cur_refill
        while (cur_refill<n and (x[cur_refill+1]-x[last_refill]<=L)):
            cur_refill+=1
        if cur_refill==last_refill:
            return -1
        if cur_refill<n:
            num_refill+=1

    return num_refill

ans = min_refills(x,n,L)
print(ans)