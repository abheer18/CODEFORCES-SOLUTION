n = int(input())
group = 1
pre = int(input())
for i in range(1,n):
        s = int(input())
        if(pre != s):
            pre = s
            group += 1
print(group)