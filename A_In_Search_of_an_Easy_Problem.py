# n = int(input())
# cnt = 0
# for i in range(n):
#     s = list(input())
#     j = 1
#     if j in s:
#         cnt += 1
#     else:
#         cnt
#     if(cnt >= 1 ):
#         print("HARD")
#     else:
#         print("EASY")

    
n = int(input())
s = list(input())
if(s.count('1') >= 1):
    print("HARD")
else:
    print("EASY")  