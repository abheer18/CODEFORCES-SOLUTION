y = int(input())
def function(y):
    while True:
        y = y+1
        if(len(set(str(y))) == len(str(y))):
            break
    return y
result = function(y)
print(result)
        
    