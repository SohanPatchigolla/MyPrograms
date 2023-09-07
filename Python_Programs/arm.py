n = int(input("Enter: "))
s = str(n)
l = len(s)
sum = 0
temp = n 
while temp >0 :
    d = temp % 10
    sum+=d**l 
    temp = temp//10
if n == sum:
    print("yes")
else:
    print("no")