n =int(input())
def arrange_coins(n):
    count = 0
    if n ==0:
        return 0
    elif n==1:
        return 1
    for i in range(1, n):
        n = n - i
        if n == 0:
            return i
        elif n < 0:
            return i-1

print(arrange_coins(n))

