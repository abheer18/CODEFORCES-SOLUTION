t = int(input())
for _ in range(t):
    num = int(input())
    if(num % 7 != 0):
        rem = num % 7 
        num = num - rem
        print(num)
    else:
        print(num)