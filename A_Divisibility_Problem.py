t = int(input())
for _ in range(t):
    a, b = map(int,input().split())
    if(a%b == 0):
        print("0")
    elif(a%b != 0):
        y = a%b
        print(b-y)