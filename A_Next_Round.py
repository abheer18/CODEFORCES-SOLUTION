n, k = map(int,input().split())
point = list(map(int,input().split()))
cnt= 0
for i in range(len(point)):
    if(point[i] >= point[k-1] and point[i] > 0):
        cnt += 1
print(cnt)