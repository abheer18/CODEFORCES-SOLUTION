n = int(input())
denom = [100,20,10,5,1]
c = 0
for x in denom:
    if n >= x:
        num = n // x
        n = n - (num * x)
        c += num
print(c)