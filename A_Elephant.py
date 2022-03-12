from cgi import print_arguments


x = int(input())
y = x//5
if(x%5==0):
    print(y)
elif(x%5 != 0):
    print(y+1)