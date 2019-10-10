# Name:        Your Name
# Student ID:  012345678

# File:        fibonacci.py

############################################################################

# the fibonacci numbers are 1,1,2,3,5,8,13,...
# fibonacci(5) should return 8 etc. (we start counting at 0)

def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-2) + fibonacci(n-1)
    
        


def main():
    # print the first ten fibonacci numbers, just as a check
    for i in range(1,10):
        print(fibonacci(i), end=' ')

main()
