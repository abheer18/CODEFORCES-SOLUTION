t = int(input())
for _ in range(t):
    myStr = list(map(int,input().split(' ')))
    cnt0 = 0
    cnt1 = 0
    for i in range(len(myStr)):
        if(myStr[i] == '0'):
            cnt0 += 1
        else:
            cnt1 += 1
    if(cnt0 > cnt1):
        print(cnt1)
    else:
        print(cnt0)
            
   