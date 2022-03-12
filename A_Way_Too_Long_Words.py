t = int(input())
for _ in range(t):
    myStr = input()
    l = len(myStr)
    if(l > 10):
        print(myStr[0]+""+str(l-2)+""+myStr[l-1])
    else:
        print(myStr)