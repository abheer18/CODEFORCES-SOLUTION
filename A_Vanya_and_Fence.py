n, h = map(int,input().split())
row = 0
while(n!=0):
    fh = list(int,input().split())
    if(fh <= h):
        row = row + 1
    else:
        row = row + 2
    n = n - 1
print(row)