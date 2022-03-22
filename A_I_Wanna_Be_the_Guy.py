# lev = int(input())
# win = 0
# x = input().split('')
# x = map(int, x)
# y = input().split('')
# y = map(int, y)
# for i in range(x):
#     if(x[i] == lev):
#         win += 1 
# for j in range(y):
#     if(y[j] == lev):
#         win += 1
# if(win >= 1):
#     print("I become the guy.")
# else:
#     print("Oh, my keyboard!")

# lev = int(input())
# for _ in range(lev):
#     x = list(map(int,input().split()))
#     y = list(map(int,input().split()))
#     if((lev in x) or (lev in y)):
#         print("I become the guy.")
#     elif((lev not in x) and (lev not in y)):
#         print("Oh, my keyboard!") 
     
n = int(input());
 
a = list(map(int, input().split()))[1:];
 
b = list(map(int, input().split()))[1:];
 
s = set(a);
 
t = set(b);
 
k = s.union(t);
 
ok = 0;
for i in range(1, n+1):
    if i in k:
        ok = 1
    else:
        ok = 0
        break
if(ok):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')