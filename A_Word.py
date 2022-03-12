word = input()
up = 0
lw = 0
for i in word:
    if(i.isupper()):
        up += 1
    elif(i.islower()):
        lw += 1
if(up > lw):
    word = word.upper()
elif(up < lw or up==lw):
    word = word.lower()
print(word)  