number = int(input())

def fibonacci_number(number):
    if number==0:
        return 0
    if number==1:
        return 1

    fib = [0,1]
    for i in range(2, number+1):
        fib.append(fib[i-1]+fib[i-2])

    return fib[-1]%10


print(fibonacci_number(number))
