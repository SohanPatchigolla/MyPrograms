n = int(input("Enter: "))

x = 0

s = str(n)
l = list(map(int, s.strip()))

for i in l:
    x = int(i)
    cube = x*x*x
    i = cube

sum = sum(l)

if n == sum:
    print(sum,"is an armstrong number")
else:
    print(sum,"is not an armstrong number")

