num1 = input()
num2 = input()
cnt = ""
for i in range(len(num1)):
    if((num1[i]=='1' and num2[i]=='0')or(num1[i]=='0' and num2[i]=='1')):
        cnt += '1'
    else:
        cnt += '0'
print(cnt)

# a=input()
# b=input()
# c=""
# for i in range(len(a)):
# 	if((a[i]=='1' and b[i]=='0')or(a[i]=='0' and b[i]=='1')):
# 		c+='1'
# 	else:
# 		c+='0'
# print (c)