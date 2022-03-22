word = input()
word = word.strip(',')
newWord = list(word)
newWord.sort()
cnt = 0
for i in range(len(newWord)):
    if(newWord[i] != '{' and newWord[i] != '}' and newWord[i] != ',' and newWord[i] != ' '):
        if(newWord[i] != newWord[i-1]):
            cnt += 1
print(cnt)

