n, W = input().split()
n, W = int(n), int(W)

values, weights = [],[]
for i in range(n):
    v, w = input().split()
    values.append(int(v))
    weights.append(int(w))


def max_values(values, weights, W):
    ans = 0
    used = []
    values_by_weight = [v/w for v, w in zip(values, weights)]
    best_weights = {b:w for b, w in zip(values_by_weight, weights)}

    while W>0:
        best = -1
        for i in range(len(values_by_weight)):
            if values_by_weight[i]>best and values_by_weight[i] not in used:
                best = values_by_weight[i]

        if best==-1:
            return ans
        wt = best_weights.get(best)
        if W>wt:
            W -= wt
            ans += wt*best
            used.append(best)
        else:
            ans += W*best
            W=0
            return ans

    return ans

ans = max_values(values, weights, W)
print(round(ans, 4))