room = int(input())
spareRoom = 0
for _ in range(room):
    p, q = map(int,input().split())
    if(q-p >=2):
        spareRoom += 1
print(spareRoom)