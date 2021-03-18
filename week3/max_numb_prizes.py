n = int(input())

def max_dis_sum(n):
    k, l = n, 1
    summands = []
    
    while k>0:
        if k<=(2*l):
            summands.append(k)
            k-=k
        else:
            summands.append(l)
            k-=l
            l+=1
    return len(summands), summands

k, summands = max_dis_sum(n)
print(k)
for s in summands:
    print(f'{s} ', end="")