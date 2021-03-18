n = int(input())
l = []
for i in range(n):
    a, b = input().split()
    a, b = int(a), int(b)
    l.append((a,b))

# The greedy choice is choosing smallest right end 
# and removing all segments that it contains

def min_join_points(lst, ans):
    l = len(lst)
    while l>0:
        a, smallest_right = lst[0]
        for i in range(len(lst)):
            a, b = lst[i]
            if b<smallest_right:
                smallest_right=b
        # ans+=str(smallest_right)
        ans.append(smallest_right)
        remove_these = []
        for i in range(len(lst)):
            a, b = lst[i]
            if smallest_right in range(a,b+1):
                remove_these.append((a,b))

        for i in range(len(remove_these)):
            lst.remove(remove_these[i])

        l = len(lst)

    return ans

ans = min_join_points(l, ans=[])
print(len(ans))
for a in ans:
    print(f'{a} ', end="")