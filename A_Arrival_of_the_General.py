n = int(input())
h = list(map(int,input().split()))
cnt = 0
for i in range(0,len(h)):
    j = i+1
    for j in range(len(h)):
        if(h[i] > h[j]):
            temp = h[i]
            h[i] = h[j]
            h[j] = temp
            cnt += 1
print(cnt)  