#prime or not prime

num = int(input("enter: ")) #input from user

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    #checking for divisibles
    for i in range(2,num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

