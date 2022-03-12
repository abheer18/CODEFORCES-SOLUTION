msg = input()
if(len(set(msg)) % 2 == 0):
    print("CHAT WITH HER!")
elif(len(set(msg)) % 2 != 0):
    print("IGNORE HIM!")