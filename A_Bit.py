n=0
x = int(input())
for i in range(x):
    a = input()
    if((a[0] == '-' and a[1] == '-') or (a[1] == '-' and a[2] == '-')):
        n = n - 1
    elif((a[0] == '+' and a[1] == '+') or (a[1] == '+' and a[2] == '+')):
        n = n + 1
    else:
        pass
print(n)
