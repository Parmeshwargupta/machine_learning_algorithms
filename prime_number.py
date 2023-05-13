n = int(input("Enter the value of n :"))
for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
    else:
        print(n, "Is not a prime number")
        break
else:
    print("The number is prime")
