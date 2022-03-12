n = int(input())
cnt = 0
col = input()
for i in range(0,n-1):
    if(col[i] == col[i+1]):
       cnt += 1
print(cnt) 