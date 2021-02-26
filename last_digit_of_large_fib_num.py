number = int(input())

def fib_number(number):
    fib = [0,1]
    for i in range(2, number+1):
        fib.append((fib[i-1]+fib[i-2])%10)

    return fib[-1]

print(fib_number(number))