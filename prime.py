# Name:        Your Name
# Student ID:  012345678

# File:        prime.py

############################################################################


# ask for a number
n = int(input("Please enter a positive integer: "))

i = 2
factorisable = False
while not factorisable and i <= n**0.5:
     if(n % i) == 0:
          factorisable = True
     else:        
          i = i + 1


if factorisable:
    print("value",n,"is not prime")
else:
    print("value",n,"is prime")
