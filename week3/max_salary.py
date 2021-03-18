n = int(input())
numbers = input().split()
numbers = [int(n) for n in numbers]

def is_greater_or_equal(max_num, cur_num):
    digit1 = str(max_num)+str(cur_num)
    digit2 = str(cur_num)+str(max_num)
    return digit2>digit1

def get_max_salary(numbers):
    ans = ""
    while len(numbers)>0:
        maxi = numbers[0]
        for i in range(len(numbers)):
            if is_greater_or_equal(maxi, numbers[i]):
                maxi = numbers[i]
        ans += str(maxi)
        numbers.remove(maxi)

    return ans

print(get_max_salary(numbers))