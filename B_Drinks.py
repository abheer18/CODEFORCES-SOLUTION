n = int(input())
sum = 0
for i in range(n):
    vol = list(map(int,input().split()))
    calVol = n*100
    sum = sum + vol[i]
    percentage = (sum/calVol)*100
print(percentage)

# n = int(input())
# sum=0
# vol = list(input().split())
# for i in range(len(vol)):
#     sum = sum + vol[i]
# calVol = n*100
# percentage = (sum//calVol)*100
# print(percentage)

