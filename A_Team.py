n = int(input())
number = 0
for i in range(n):
    Petya, Vasya, Tonya = map(int,input().split())
    if(Petya + Vasya + Tonya >= 2):
        number += 1
print(number)   