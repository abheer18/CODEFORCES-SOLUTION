n = int(input())
cap = 0
inTram = 0
for _ in range(n):
    ex, en = map(int,input().split())
    inTram = inTram - ex
    inTram = inTram + en
    cap = max(cap,inTram)
print(cap)