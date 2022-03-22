color = list(input())
color.sort()
shoe = 0
for i in range(0,4):
    if(color[i] == color[i+1]):
        shoe += 1
    elif(color[i] != color[i+1]):
        shoe += 0
print(4-shoe)