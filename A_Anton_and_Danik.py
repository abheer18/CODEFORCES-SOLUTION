# n = int(input())
# score = input()
# a=0
# d=0
# for i in range(len(score)):
#     a = a + score.count('A')
#     d = d + score.count('D')
# if(a>d):
#     print("Anton")
# if(a==d):
#     print("Friendship")
# if(a<d):
#     print("Danik")

# n = int(input())
# for _ in range(n):
#     score = list(input())
#     for i in range(len(score)):
#         a = score.count('A')
#         d = score.count('D')
# if(a>d):
#     print("Anton")
# elif(a<d):
#     print("Danik")
# elif(a==d):
#     print("Friendship")

a=int(input())
b=input()
ans=b.count('A')
ans1=b.count('D')
if ans>ans1:
	print("Anton")
if ans<ans1:
	print ("Danik")
if ans==ans1:
	print ("Friendship")
