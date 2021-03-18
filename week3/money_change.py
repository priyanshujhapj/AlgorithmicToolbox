def money_change(m):
    change = []
    while m>0:
        if m>=10:
            m-=10
            change.append(10)
        elif m>=5:
            m-=5
            change.append(5)
        else:
            m-=1
            change.append(1)

    return len(change)

print(money_change(int(input())))