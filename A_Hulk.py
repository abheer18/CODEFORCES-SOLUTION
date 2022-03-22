# n = int(input()
# for i in range(1,n):
# 	if i%2 == 1:
# 		print ("I hate that"),
# 	else:
# 		print ("I love that"),
# if n%2 == 1:
# 	print ("I hate it")
# else:
# 	print ("I love it")

n = int(input())
a = ["I hate", "I love"] * n
print(" that ".join(a[0:n]),"it")